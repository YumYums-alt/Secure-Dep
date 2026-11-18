import requests

from src.fetcher import get_status_code


class FakeResponse:
    status_code = 200


def test_get_status_code_returns_status(monkeypatch):
    seen = {}

    def fake_get(url, timeout):
        seen["url"] = url
        seen["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr(requests, "get", fake_get)

    assert get_status_code("https://example.com") == 200
    assert seen["url"] == "https://example.com"
    assert seen["timeout"] == 5.0
