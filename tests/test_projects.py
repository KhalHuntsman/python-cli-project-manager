#!/usr/bin/env python3

# Author
# Date: 12/9/25
# Version 1.1

"""
Unit tests for the Project model.
"""

from models.user import User
from models.project import Project


def test_project_creation():
    u = User("Charlie", "charlie@example.com")
    p = Project("Build App", "Test desc", "2025-12-31", u.id)

    assert p.title == "Build App"
    assert p.user_id == u.id
    assert isinstance(p.tasks, list)
    assert p in u.projects


def test_project_add_task_relationship():
    u = User("Dana", "dana@example.com")
    p = Project("Test Project", "desc", "2030-01-01", u.id)

    class FakeTask:
        pass

    t = FakeTask()
    p.add_task(t)

    assert t in p.tasks
