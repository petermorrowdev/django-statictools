import logging

from django.apps import AppConfig
from django.conf import settings

from statictools.conf import get_settings
from statictools.manifest import StaticManifest


logger = logging.getLogger(__name__)


class StatictoolsConfig(AppConfig):
    name = 'statictools'
    verbose_name = "Static Tools"
    
    def ready(self):
        logger.info(f"Starting statictools {get_settings()}")
        if not get_settings().enable_hmr:
            StaticManifest.load()
