import logging

from django.shortcuts import redirect
from django.http.response import Http404
from django.contrib.staticfiles.views import serve

from statictools.assets import generate_vite_asset_url


logger = logging.getLogger(__name__)


def vite_static_redirect(request, path, insecure=False):
    try:
        response = serve(request, path, insecure)
    except Http404:
        vite_dev_url = generate_vite_asset_url(path)
        if vite_dev_url is not None:
            return redirect(vite_dev_url, permanent=False)
        else:
            raise Http404
    else:
        return response
