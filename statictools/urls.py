from urllib.parse import urljoin

from statictools.conf import get_settings


def generate_dev_url(path):
    s = get_settings()
    return urljoin(f'{s.hmr_proto}://{s.hmr_host}:{s.hmr_port}/', path)
