from dataclasses import dataclass
from pathlib import Path
from typing import Any

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
    
    @property
    def hmr_endpoint(self) -> str:
        return f'{self.hmr_proto}://{self.hmr_host}:{self.hmr_port}/'


default_settings = StatictoolsSettings()


def get_settings() -> StatictoolsSettings:
    s: dict[str, Any] | None = getattr(django_settings, "STATICTOOLS", None)
    if s is not None:
        return StatictoolsSettings(
            assets_path=Path(s.get('assets_path', default_settings.assets_path)),
            enable_hmr=bool(s.get('enable_hmr', default_settings.enable_hmr)),
            hmr_proto=str(s.get('hmr_proto', default_settings.hmr_proto)),
            hmr_host=str(s.get('hmr_host', default_settings.hmr_host)),
            hmr_port=int(s.get('hmr_port', default_settings.hmr_port)),
        )
    else:
        return default_settings
