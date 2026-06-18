from django.shortcuts import render

from .conf import panel_config


@panel_config.permission_required("index")
def index(request):
    context = panel_config.get_context(request, title="DOOM")
    return render(request, "admin/dj_doom_panel/index.html", context)
