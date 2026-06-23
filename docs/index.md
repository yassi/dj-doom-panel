# dj-doom-panel

![dj-doom-panel](https://raw.githubusercontent.com/yassi/dj-doom-panel/main/images/dj-doom-panel.png)

**The Django admin panel that matters.**

`dj-doom-panel` adds a fully playable, original DOOM panel to your Django admin interface. It sits right there in your sidebar, between your cache monitor and your Celery queue.

![DOOM gameplay in Django admin](https://raw.githubusercontent.com/yassi/dj-doom-panel/main/images/doom-gameplay.png)

The panel embeds [js-dos v8](https://js-dos.com), a DOSBox-powered DOS emulator that runs in the browser via WebAssembly. The game bundle is the original DOOM shareware release, which id Software made freely available in 1997. No WAD files are bundled with this package.

## Quick links

- [Installation](installation.md)
- [Configuration](configuration.md)

## Requirements

- Python 3.9+
- Django 4.2+
- [dj-control-room-base](https://github.com/yassi/dj-control-room-base) >= 1.0.0
- [dj-control-room](https://github.com/yassi/dj-control-room) >= 1.3.0

## License

MIT. See [LICENSE](https://github.com/yassi/dj-doom-panel/blob/main/LICENSE).

---

DOOM is a trademark of id Software LLC. dj-doom-panel is an unaffiliated fan project and is not endorsed by id Software, ZeniMax, or Bethesda.
