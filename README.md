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

Because the real question was never "does it scale?" — it was "can it run Doom?"

`dj-doom-panel` adds a fully playable, original DOOM panel to your Django admin interface. It sits right there in your sidebar, between your cache monitor and your Celery queue — just where it belongs.

---

## Installation

```bash
pip install dj-doom-panel, dj-control-room
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

## Requirements

- Django 4.2+
- [dj-control-room](https://github.com/yassi/dj-control-room) ≥ 1.3.0
- [dj-control-room-base](https://github.com/yassi/dj-control-room-base) ≥ 1.0.0
- An internet connection (the game loads from [js-dos.com](https://js-dos.com))

---

## How it works

![DOOM gameplay in Django admin](https://raw.githubusercontent.com/yassi/dj-doom-panel/main/images/doom-gameplay.png)

The panel embeds [js-dos v8](https://js-dos.com) — a DOSBox-powered DOS emulator that runs in the browser via WebAssembly. The game bundle is the original DOOM shareware release, which id Software made freely available in 1997.

No WAD files are bundled with this package. The game is loaded from the js-dos CDN at runtime.

### CSP note

If your project uses a Content Security Policy, you'll need to allow `v8.js-dos.com` for `script-src`, `style-src`, `connect-src`, and `worker-src`.

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

`dj-doom-panel` is a plugin for [dj-control-room](https://github.com/yassi/dj-control-room) — a framework for building operational admin panels in Django. Other panels in the ecosystem include cache inspection, Redis monitoring, and Celery queue management.

All critically important, of course.

---

## License

MIT
