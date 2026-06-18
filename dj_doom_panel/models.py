from dj_control_room_base.core import PanelPlaceholderModel


class DoomPanelPlaceholder(PanelPlaceholderModel):
    class Meta(PanelPlaceholderModel.Meta):
        verbose_name = "DOOM"
        verbose_name_plural = "DOOM"
