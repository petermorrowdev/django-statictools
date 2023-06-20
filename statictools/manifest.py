import os
import json
import logging
from contextvars import ContextVar
from typing import Dict, Any

from statictools.conf import get_settings


logger = logging.getLogger(__name__)


class StaticManifest:
    _manifest_data: Dict[str, Any] | None = None
    
    @classmethod
    def load(cls):
        cls._manifest_data = read_manifest()
    
    @classmethod
    def get(cls):
        if cls._manifest_data is not None:
            return cls._manifest_data
        else:
            raise RuntimeError("manifest.json is not loaded")


def read_manifest():
    s = get_settings()
    try:
        logger.info(f'Reading manifest from "{s.manifest_path}"')
        with open(s.manifest_path) as f:
            return json.load(f)
    except FileNotFoundError:
        RuntimeError(f'manifest.json not found in "{s.manifest_path}"')


def get_manifest() -> dict:
    return StaticManifest.get()
