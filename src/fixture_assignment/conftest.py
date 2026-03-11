import logging
import pytest
import os

@pytest.fixture(autouse=True)
def setup():
    os.environ["APP_ENV"]="test"
    logging.basicConfig(level=logging.DEBUG)

@pytest.fixture()
def fake_user():
    dict1={"id" : 101, "name": "priya"}
    return dict1


class InMemoryRepo:
    def __init__(self):
        self._items = {}

    def add(self, key, value):
        if key in self._items:
            raise KeyError("duplicate")
        self._items[key] = value

    def get(self, key):
        return self._items[key]

    def clear(self):
        self._items.clear()

@pytest.fixture(scope="function")
def repo_user():
    repo = InMemoryRepo()
    yield repo
    repo.clear()




