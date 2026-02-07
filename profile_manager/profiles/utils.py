from configparser import NoSectionError, RawConfigParser
from pathlib import Path
from sys import platform
from typing import Any, Dict, List, Optional

import pyplugin_installer
from qgis.core import QgsUserProfileManager
from qgis.utils import iface

from profile_manager.qdt_export.models import QdtPluginInformation


def qgis_profiles_path() -> Path:
    """Get QGIS profiles paths from current QGIS application

    Returns:
        Path: QGIS profiles path
    """
    return Path(iface.userProfileManager().rootLocation())


def get_profile_qgis_ini_path(profile_name: str) -> Path:
    """Get QGIS3.ini file path for a profile

    Args:
        profile_name (str): profile name

    Returns:
        Path: QGIS3.ini path
    """
    # MacOS
    if platform.startswith("darwin"):
        return qgis_profiles_path() / profile_name / "qgis.org" / "QGIS3.ini"
    # Windows / Linux
    return qgis_profiles_path() / profile_name / "QGIS" / "QGIS3.ini"


def get_profile_plugin_metadata_path(profile_name: str, plugin_slug_name: str) -> Path:
    """Get path to metadata.txt for a plugin inside a profile

    Args:
        profile_name (str): profile name
        plugin_slug_name (str): plugin slug name

    Returns:
        Path: metadata.txt path
    """
    return (
        qgis_profiles_path()
        / profile_name
        / "python"
        / "plugins"
        / plugin_slug_name
        / "metadata.txt"
    )


def get_installed_plugin_list(
    profile_name: str, only_activated: bool = True
) -> List[str]:
    """Get installed plugin for a profile

    Args:
        profile_name (str): profile name
        only_activated (bool, optional): True to get only activated plugin, False to get all installed plugins. Defaults to True.

    Returns:
        List[str]: plugin slug name list
    """
    ini_parser = RawConfigParser()
    ini_parser.optionxform = str  # str = case-sensitive option names
    ini_parser.read(get_profile_qgis_ini_path(profile_name))
    try:
        plugins_in_profile = dict(ini_parser.items("PythonPlugins"))
    except NoSectionError:
        plugins_in_profile = {}

    if only_activated:
        return [key for key, value in plugins_in_profile.items() if value == "true"]
    else:
        return plugins_in_profile.keys()


def get_installed_plugin_metadata(
    profile_name: str, plugin_slug_name: str
) -> Dict[str, Any]:
    """Get metadata information from metadata.txt file in profile installed plugin

    Args:
        profile_name (str): profile name
        plugin_slug_name (str): plugin slug name

    Returns:
        Dict[str, Any]: metadata as dict. Empty dict if metadata unavailable
    """
    ini_parser = RawConfigParser()
    ini_parser.optionxform = str  # str = case-sensitive option names
    plg_metadata_path = get_profile_plugin_metadata_path(profile_name, plugin_slug_name)
    ini_parser.read(plg_metadata_path)
    try:
        metadata = dict(ini_parser.items("general"))
        metadata["folder_name"] = plg_metadata_path.parent.name
    except NoSectionError:
        metadata = {}
    return metadata


def get_plugin_info_from_qgis_manager(
    plugin_slug_name: str, reload_manager: bool = False
) -> Optional[Dict[str, str]]:
    """Get plugin informations from QGIS plugin manager

    Args:
        plugin_slug_name (str): _description_
        reload_manager (bool, optional): reload manager for new plugins. Defaults to False.

    Returns:
        Optional[Dict[str, str]]: metadata from plugin manager, None if plugin not found
    """
    if reload_manager:
        pyplugin_installer.instance().reloadAndExportData()
    return iface.pluginManagerInterface().pluginMetadata(plugin_slug_name)


def get_profile_name_list() -> List[str]:
    """Get profile name list from current installed QGIS

    Returns:
        List[str]: profile name list
    """
    return QgsUserProfileManager(qgis_profiles_path()).allProfiles()


def define_plugin_version_from_metadata(
    manager_metadata: Dict[str, Any], plugin_metadata: Dict[str, Any]
) -> str:
    """Define plugin version from available metadata

    Args:
        manager_metadata (Dict[str, Any]): QGIS plugin manager metadata
        plugin_metadata (Dict[str, Any]): installed plugin metadata

    Returns:
        str: plugin version
    """
    # Use version from plugin metadata
    if "version" in plugin_metadata:
        return plugin_metadata["version"]

    # Fallback to stable version
    if manager_metadata["version_available_stable"]:
        return manager_metadata["version_available_stable"]
    # Fallback to experimental version
    if manager_metadata["version_available_experimental"]:
        return manager_metadata["version_available_experimental"]
    # Fallback to available version
    if manager_metadata["version_available"]:
        return manager_metadata["version_available"]
    # No version defined
    return ""


def get_profile_plugin_information(
    profile_name: str, plugin_slug_name: str
) -> Optional[QdtPluginInformation]:
    """Get plugin information from profile. Only official plugin are supported.

    Args:
        profile_name (str): profile name
        plugin_slug_name (str):  plugin slug name

    Returns:
        Optional[PluginInformation]: plugin information, None if plugin is not official
    """
    manager_metadata = get_plugin_info_from_qgis_manager(
        plugin_slug_name=plugin_slug_name
    )

    plugin_metadata = get_installed_plugin_metadata(
        profile_name=profile_name, plugin_slug_name=plugin_slug_name
    )

    if manager_metadata is None and plugin_metadata is None:
        print(f"Plugin {plugin_slug_name} not found in profile {profile_name}")
        return None

    if manager_metadata is None:
        manager_metadata = {
            "name": plugin_metadata.get("name", plugin_slug_name),
            "download_url": None,
            "plugin_id": None,
            "folder_name": plugin_metadata.get("folder_name", plugin_slug_name),
        }

    return QdtPluginInformation(
        name=manager_metadata.get("name", plugin_slug_name),
        download_url=manager_metadata.get("download_url"),
        folder_name=plugin_metadata.get("folder_name", plugin_slug_name),
        plugin_id=(
            int(manager_metadata["plugin_id"])
            if manager_metadata["plugin_id"]
            else None
        ),
        version=define_plugin_version_from_metadata(
            manager_metadata=manager_metadata,
            plugin_metadata=plugin_metadata,
        ),
    )


def get_profile_plugin_list_information(
    profile_name: str, only_activated: bool = True
) -> List[QdtPluginInformation]:
    """Get profile plugin information

    Args:
        profile_name (str): profile name
        only_activated (bool, optional): True to get only activated plugin, False to get all installed plugins. Defaults to True.

    Returns:
        List[PluginInformation]: list of PluginInformation
    """
    plugin_list: List[str] = get_installed_plugin_list(
        profile_name=profile_name, only_activated=only_activated
    )

    # Get information about installed plugin
    profile_plugin_list: List[QdtPluginInformation] = []
    for plugin_name in plugin_list:
        plugin_info = get_profile_plugin_information(profile_name, plugin_name)
        if plugin_info and plugin_info.plugin_id:
            profile_plugin_list.append(plugin_info)
        elif plugin_info and not plugin_info.plugin_id:
            profile_plugin_list.append(plugin_info)

    return profile_plugin_list
