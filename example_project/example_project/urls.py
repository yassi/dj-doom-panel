from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        "admin/dj-doom-panel/",
        include("dj_doom_panel.urls"),
    ),
    path("admin/dj-control-room-base/", include("dj_control_room_base.urls")),
    path("admin/dj-control-room/", include("dj_control_room.urls")),
    path("admin/", admin.site.urls),
]
