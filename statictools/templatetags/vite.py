from typing import Dict

from django import template
from django.utils.safestring import mark_safe

from statictools.assets import generate_vite_asset
from statictools.conf import get_settings
from statictools.tags import generate_script_tag
from statictools.urls import generate_dev_url


register = template.Library()


@register.simple_tag
@mark_safe
def vite_hmr_client() -> str:
    s = get_settings()
    if s.enable_hmr:
        url = generate_dev_url(s.client_lib)
        return generate_script_tag(url, {"type": "module"})
    else:
        return ""


@register.simple_tag
@mark_safe
def vite_asset(
    path: str,
    **kwargs: Dict[str, str],
) -> str:
    assert path is not None

    return generate_vite_asset(path, **kwargs)
