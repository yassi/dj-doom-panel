from django.contrib import admin
from dj_control_room_base.core import BasePanelAdmin

from .conf import panel_config
from .models import DoomPanelPlaceholder


@admin.register(DoomPanelPlaceholder)
class DoomPanelPlaceholderAdmin(BasePanelAdmin):
    redirect_url_name = "dj_doom_panel:index"
    panel_config = panel_config
