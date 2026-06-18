"""
DJ Control Room panel plugin for dj-doom-panel.

Registers this package with the hub via the entry point defined in
``pyproject.toml`` under ``[project.entry-points."dj_control_room.panels"]``.
"""

from dj_control_room_base.core import PanelPlugin


class DoomPanel(PanelPlugin):
    name = "DOOM"
    description = "Mission-critical operations dashboard"
    icon = "dj_doom_panel/images/doomguy-face.png"
    icon_color = ""

    app_name = "dj_doom_panel"
    docs_url = "https://github.com/yassi/dj-doom-panel"
    pypi_url = "https://pypi.org/project/dj-doom-panel/"

    def get_config(self):
        from .conf import panel_config

        return panel_config
