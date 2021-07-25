"""
Enterprise provides a set of general Enterprise services.
"""
from pathlib import Path
import os
from diagrams import Node


class _Enterprise(Node):
    _provider = "enterprise"
    _icon_dir = "resources/enterprise"

    fontcolor = "#ffffff"


class _Networkservices(_Enterprise):
    _type = "networkservices"
    _icon_dir = "resources/enterprise/network"


class PaloFW(_Networkservices):
    _icon = "palofw.png"

    def _load_icon(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent, self._icon_dir, self._icon)
