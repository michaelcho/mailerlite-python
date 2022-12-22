import pytest


def pytest_configure():
    return {"entity_id": 0, "entity_email": "random@mailerlite.com"}
