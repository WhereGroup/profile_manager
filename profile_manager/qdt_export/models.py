from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class QdtPluginInformation:
    """QGIS Plugin representation for QDT profile export."""

    name: str
    folder_name: str
    version: str
    download_url: Optional[str] = None
    plugin_id: Optional[int] = None

    def as_dict(self) -> Dict[str, Any]:
        """Custom as_dict method to handle properties and specific vars.

        :return: dict of PluginInformation
        :rtype: Dict[str, Any]
        """
        out_dict = {
            "name": self.name,
            "folder_name": self.folder_name,
            "official_repository": self.official_repository,
            "plugin_id": self.plugin_id,
            "version": self.version,
        }
        if not self.official_repository and self.download_url:
            out_dict["url"] = self.download_url

        return out_dict

    @property
    def official_repository(self) -> bool:
        """Check if plugin is from official QGIS repository.

        :return: True if plugin is from official QGIS repository.
        :rtype: bool
        """
        if self.download_url is None:
            return False
        return self.download_url.startswith("https://plugins.qgis.org")


@dataclass
class QDTProfileInfos:
    """Store informations for QDT profile creation"""

    description: str = ""
    email: str = ""
    version: str = ""
    qgis_min_version: str = ""
    qgis_max_version: str = ""
