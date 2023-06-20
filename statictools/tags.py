from typing import Any

from django.conf import settings
from urllib.parse import urljoin


def generate_script_tag(src: str, attrs: dict[str, str]) -> str:
    attrs_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])
    return f'<script {attrs_str} src="{src}"></script>'


def generate_stylesheet_tag(href: str) -> str:
    return f'<link rel="stylesheet" href="{href}" />'


def generate_css_tags_for_entry(
    manifest_entry: dict[str, Any],
    already_processed: list[str],
) -> list[str]:
    tags = []

    if "imports" in manifest_entry:
        for import_path in manifest_entry["imports"]:
            tags.extend(generate_css_tags_for_entry(urljoin(settings.STATIC_URL, import_path), already_processed))

    if "css" in manifest_entry:
        for css_path in manifest_entry["css"]:
            if css_path not in already_processed:
                tags.append(
                    generate_stylesheet_tag(urljoin(settings.STATIC_URL, css_path))
                )

            already_processed.append(css_path)

    return tags
