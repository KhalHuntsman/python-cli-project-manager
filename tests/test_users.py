#!/usr/bin/env python3

# Author
# Date: 12/9/25
# Version 1.1

"""
Unit tests for the User model.
"""

from models.user import User


def test_user_creation():
    u = User("Alice", "alice@example.com")
    assert u.name == "Alice"
    assert u.email == "alice@example.com"
    assert u.id >= 1
    assert isinstance(u.projects, list)


def test_user_add_project_relationship():
    u = User("Bob", "bob@example.com")
    # fake project object
    class FakeProject:
        pass

    p = FakeProject()
    u.add_project(p)

    assert p in u.projects
