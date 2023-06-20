from typing import Dict
from urllib.parse import urljoin

from django.conf import settings

from statictools.conf import get_settings
from statictools.manifest import get_manifest
from statictools.tags import generate_script_tag, generate_css_tags_for_entry
from statictools.urls import generate_dev_url


def generate_vite_asset_url(path: str) -> str:
    if get_settings().enable_hmr:
        return generate_dev_url(path)
    
    manifest = get_manifest()
    return urljoin(settings.STATIC_URL, manifest[path]["file"])


def generate_vite_asset(path: str, **attrs: Dict[str, str]) -> str:
    if get_settings().enable_hmr:
        return generate_script_tag(generate_dev_url(path), {"type": "module"})
    else:
        tags = []
        manifest = get_manifest()
        manifest_entry = manifest[path]
        scripts_attrs = {"type": "module", **attrs}

        tags.extend(generate_css_tags_for_entry(manifest_entry, []))

        for entry_import in manifest_entry.get('imports', []):
            tags.extend(generate_css_tags_for_entry((manifest[entry_import]), []))

        tags.append(
            generate_script_tag(
                urljoin(settings.STATIC_URL, manifest_entry["file"]),
                attrs=scripts_attrs,
            )
        )
        return "\n".join(tags)
