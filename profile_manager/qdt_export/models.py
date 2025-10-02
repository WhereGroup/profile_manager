from dataclasses import dataclass


@dataclass
class QDTProfileInfos:
    """Store informations for QDT profile creation"""

    description: str = ""
    email: str = ""
    version: str = ""
    qgis_min_version: str = ""
    qgis_max_version: str = ""
