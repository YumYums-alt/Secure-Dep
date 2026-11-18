"""Tiny helper that uses the requests library, so the dependency is real."""

import requests


def get_status_code(url, timeout=5.0):
    """Fetch url and return the HTTP status code.

    A timeout is always set. Without one, requests can hang forever,
    and bandit flags that as a medium-severity issue.
    """
    response = requests.get(url, timeout=timeout)
    return response.status_code
