#!/usr/bin/env python3

# Author
# Date: 12/9/25
# Version 1.1

"""
Unit tests for the Task model.
"""

from models.user import User
from models.project import Project
from models.task import Task


def test_task_creation():
    u = User("Evan", "evan@example.com")
    p = Project("Project X", "desc", "2030-01-01", u.id)
    t = Task("Do something", "Evan", p.id)

    assert t.title == "Do something"
    assert t.assigned_to == "Evan"
    assert t.project_id == p.id
    assert t in p.tasks


def test_mark_complete():
    u = User("Frank", "frank@example.com")
    p = Project("Proj", "d", "2030-01-01", u.id)
    t = Task("Test task", "Frank", p.id)

    t.mark_complete()
    assert t.status == "completed"
