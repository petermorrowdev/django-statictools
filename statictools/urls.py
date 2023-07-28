from urllib.parse import urljoin

from statictools.conf import get_settings


def generate_dev_url(path):
    s = get_settings()
    return urljoin(s.hmr_endpoint, path)
