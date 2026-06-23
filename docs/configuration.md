# Configuration

All configuration is done through a single `DJ_DOOM_PANEL_SETTINGS` dict in your Django settings file. Every key is optional; the defaults work out of the box.

```python
# settings.py
DJ_DOOM_PANEL_SETTINGS = {
    "ALLOWED_GROUPS": [],
    "REQUIRE_SUPERUSER": False,
    "LOAD_DEFAULT_CSS": True,
    "EXTRA_CSS": [],
}
```

---

## Access control

Permission enforcement is provided by [dj-control-room-base](https://github.com/yassi/dj-control-room-base). By default, any staff user (`is_staff=True`) can access the panel. Anonymous users are redirected to the Django admin login.

| Setting | Type | Default | Description |
|---|---|---|---|
| `ALLOWED_GROUPS` | `list[str]` | `[]` | Django group names allowed to access the panel. An empty list means any staff user is allowed. |
| `REQUIRE_SUPERUSER` | `bool` | `False` | When `True`, restricts access to superusers only. |

Superusers always bypass group checks, consistent with standard Django admin behaviour.

### Examples

Restrict to superusers only:

```python
DJ_DOOM_PANEL_SETTINGS = {
    "REQUIRE_SUPERUSER": True,
}
```

Restrict to members of specific groups:

```python
DJ_DOOM_PANEL_SETTINGS = {
    "ALLOWED_GROUPS": ["ops", "devs"],
}
```

---

## CSS settings

| Setting | Type | Default | Description |
|---|---|---|---|
| `LOAD_DEFAULT_CSS` | `bool` | `True` | Loads the shared design-system stylesheet from `dj-control-room-base`. Set to `False` if a parent template already loads it. |
| `EXTRA_CSS` | `list[str]` | `[]` | Additional stylesheets to inject. Relative paths are resolved through Django's staticfiles system; absolute URLs are used as-is. |

```python
DJ_DOOM_PANEL_SETTINGS = {
    "LOAD_DEFAULT_CSS": True,
    "EXTRA_CSS": [
        "myapp/css/overrides.css",
        "https://cdn.example.com/theme.css",
    ],
}
```

---

## CSP note

If your project uses a Content Security Policy, you need to allow `v8.js-dos.com` for `script-src`, `style-src`, `connect-src`, and `worker-src`. The game bundle is loaded from the js-dos CDN at runtime.
