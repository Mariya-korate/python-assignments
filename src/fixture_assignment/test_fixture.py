import logging

import os

def test_user(fake_user):
    logging.debug(f"Before update: {fake_user}")
    fake_user["id"] = 102
    logging.debug(f"After update: {fake_user}")
    assert  fake_user["id"] == 102

def test_setup(setup):
    assert "APP_ENV" in os.environ
    print(os.environ["APP_ENV"])

def test_repo(repo_user):
    repo_user.add(1, "priya")
    assert repo_user.get(1)=="priya"
    print(repo_user._items)

def test_repo_invalid(repo_user):
    # print(repo_user._items)
    assert repo_user._items=={}
    print(repo_user._items)



