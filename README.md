[![Tests](https://github.com/yassi/dj-doom-panel/actions/workflows/test.yml/badge.svg)](https://github.com/yassi/dj-doom-panel/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/yassi/dj-doom-panel/branch/main/graph/badge.svg)](https://codecov.io/gh/yassi/dj-doom-panel)
[![PyPI version](https://badge.fury.io/py/dj-doom-panel.svg)](https://badge.fury.io/py/dj-doom-panel)
[![Python versions](https://img.shields.io/pypi/pyversions/dj-doom-panel.svg)](https://pypi.org/project/dj-doom-panel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/dj-doom-panel.svg)](https://pypi.org/project/dj-doom-panel/)
[![Django Control Room Panel](https://img.shields.io/badge/Django%20Control%20Room-Panel-0c4b33?logo=django)](https://github.com/yassi/dj-control-room)


# Django Doom Panel

![dj-doom-panel](https://raw.githubusercontent.com/yassi/dj-doom-panel/main/images/dj-doom-panel.png)

**The Django admin panel that matters.**

Every project eventually asks the same question: Can it run DOOM?

Yes. Yes it can.

`dj-doom-panel` adds a fully playable DOOM panel to your Django admin interface. It sits right there in your sidebar, between your cache monitor and your Celery queue. Just where it belongs.

---

## Installation

```bash
pip install dj-doom-panel dj-control-room
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "dj_control_room_base",
    "dj_doom_panel",
    "dj_control_room",
    ...
]
```

Add to `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path("admin/dj-doom-panel/", include("dj_doom_panel.urls")),
    path("admin/dj-control-room-base/", include("dj_control_room_base.urls")),
    path("admin/dj-control-room/", include("dj_control_room.urls")),
    path("admin/", admin.site.urls),
]
```

That's it. Open your admin. Click DOOM.

---

## Configuration

All settings are optional. Add a `DJ_DOOM_PANEL_SETTINGS` dict to your Django settings to override any of them:

```python
DJ_DOOM_PANEL_SETTINGS = {
    "ALLOWED_GROUPS": [],
    "REQUIRE_SUPERUSER": False,
    "LOAD_DEFAULT_CSS": True,
    "EXTRA_CSS": [],
}
```

### Access control

By default, any staff user can access the panel. The permission settings below are inherited from [dj-control-room-base](https://github.com/yassi/dj-control-room-base).

| Setting | Type | Default | Description |
|---|---|---|---|
| `ALLOWED_GROUPS` | `list[str]` | `[]` | Django group names allowed to access the panel. An empty list means any staff user is allowed. |
| `REQUIRE_SUPERUSER` | `bool` | `False` | Restrict the panel to superusers only. |

Superusers always bypass group checks.

### CSS

| Setting | Type | Default | Description |
|---|---|---|---|
| `LOAD_DEFAULT_CSS` | `bool` | `True` | Load the shared design-system stylesheet. Set to `False` if a parent template already loads it. |
| `EXTRA_CSS` | `list[str]` | `[]` | Additional stylesheets to inject. Relative paths resolve through Django's staticfiles; absolute URLs are used as-is. |

---

## Requirements

- Django 4.2+
- [dj-control-room](https://github.com/yassi/dj-control-room) >= 1.3.0
- [dj-control-room-base](https://github.com/yassi/dj-control-room-base) >= 1.0.0

---

## How it works

![DOOM gameplay in Django admin](https://raw.githubusercontent.com/yassi/dj-doom-panel/main/images/doom-gameplay.png)

The panel embeds [js-dos v8](https://js-dos.com) — a DOSBox-powered DOS emulator that runs in the browser via WebAssembly. The game bundle (`DOOM1.WAD` + `DOOM.EXE`) is the **DOOM shareware v1.9**, which id Software has explicitly made freely distributable.

The bundle is shipped as a Django static file and served directly from your own application — no external CDN required. The game works offline once your static files are collected.

### CSP note

If your project uses a Content Security Policy, you'll need to allow `v8.js-dos.com` for `script-src`, `style-src`, `connect-src`, and `worker-src` (for the js-dos emulator runtime itself).

---

## Controls

| Key | Action |
|-----|--------|
| Arrow keys | Move / turn |
| Ctrl | Fire |
| Space | Use / open |
| Shift | Run |
| Alt + Arrow | Strafe |

---

## Part of the dj-control-room ecosystem

`dj-doom-panel` is a plugin for [dj-control-room](https://github.com/yassi/dj-control-room), a framework for building operational admin panels in Django. Other panels in the ecosystem include cache inspection, Redis monitoring, and Celery queue management.

All critically important, of course.

---

## License

MIT

---

DOOM is a trademark of id Software LLC. dj-doom-panel is an unaffiliated fan project and is not endorsed by id Software, ZeniMax, or Bethesda.
