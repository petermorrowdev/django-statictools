import logging

from django.apps import AppConfig

from statictools.conf import get_settings
from statictools.manifest import StaticManifest


logger = logging.getLogger(__name__)


class StatictoolsConfig(AppConfig):
    name = 'statictools'
    verbose_name = "Static Tools"
    
    def ready(self):
        statictools_settings = get_settings()
        logger.info(f"Redirecting assets to HMR {statictools_settings.hmr_endpoint}")
        if not get_settings().enable_hmr:
            StaticManifest.load()
