# Installation

## 1. Install the package

```bash
pip install dj-doom-panel
```

## 2. Add to `INSTALLED_APPS`

```python
INSTALLED_APPS = [
    ...
    "dj_control_room_base",
    "dj_doom_panel",
    "dj_control_room",
    ...
]
```

`dj_control_room_base` provides the shared design system and permission infrastructure. `dj_control_room` is the hub that registers and surfaces all panels in the admin sidebar.

## 3. Add URLs

```python
from django.urls import path, include

urlpatterns = [
    path("admin/dj-doom-panel/", include("dj_doom_panel.urls")),
    path("admin/dj-control-room-base/", include("dj_control_room_base.urls")),
    path("admin/dj-control-room/", include("dj_control_room.urls")),
    path("admin/", admin.site.urls),
]
```

## 4. Run migrations

```bash
python manage.py migrate
```

This creates the placeholder model entry that wires the panel into the Django admin sidebar.

## 5. Open the admin

Start your development server and navigate to `/admin/`. A **DOOM** entry appears in the sidebar and links to the panel.
