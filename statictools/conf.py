from dataclasses import dataclass
from pathlib import Path

from django.conf import settings as django_settings


@dataclass
class StatictoolsSettings:
    assets_path: Path = Path("./static")

    enable_hmr: bool = django_settings.DEBUG
    hmr_proto: str = "http"
    hmr_host: str = "127.0.0.1"
    hmr_port: int = 3000

    @property
    def static_root(self) -> Path:
        if self.enable_hmr:
            return self.assets_path
        else:
            return Path(getattr(django_settings, "STATIC_ROOT", "./dist") or "./dist")

    @property
    def manifest_path(self) -> Path:
        return self.static_root / 'manifest.json'
    
    @property
    def client_lib(self) -> str:
        return '@vite/client'


default_settings = StatictoolsSettings()


def get_settings():
    return getattr(django_settings, "STATICTOOLS_SETTINGS", default_settings)
