#!/usr/bin/env python3
# Author
# Date: 12/9/25 
# Version 1.1
"""
Utility functions for saving and loading model data using JSON files.

Provides a clean separation between file I/O logic and the rest of the
application. Supports saving and loading Users, Projects, and Tasks by
serializing model instances into dictionaries and reconstructing them
from stored JSON data.
"""

import json
import os

from models.user import User
from models.project import Project
from models.task import Task


# -------------------- FILE PATHS --------------------
DATA_DIR = "data"

USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")


# -------------------- GENERIC JSON HELPERS --------------------
def load_json(path):
    """Load JSON data from a file. If the file does not exist, return an empty list."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Warning: {path} is corrupted. Starting with empty data.")
        return []


def save_json(path, data):
    """Save Python data (list/dict) into a JSON file."""
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


# -------------------- SAVE FUNCTIONS --------------------
def save_users():
    """Convert all user objects to dictionaries and save them to JSON."""
    data = [u.to_dict() for u in User.get_all()]
    save_json(USERS_FILE, data)


def save_projects():
    """Convert all project objects to dictionaries and save them to JSON."""
    data = [p.to_dict() for p in Project.get_all()]
    save_json(PROJECTS_FILE, data)


def save_tasks():
    """Convert all task objects to dictionaries and save them to JSON."""
    data = [t.to_dict() for t in Task.get_all()]
    save_json(TASKS_FILE, data)


def save_all():
    """Convenience helper to save everything at once."""
    save_users()
    save_projects()
    save_tasks()


# -------------------- LOAD FUNCTIONS --------------------
def load_users():
    """Load user dictionaries from JSON and rebuild User instances."""
    data = load_json(USERS_FILE)

    # Reset class-level data before loading
    User._users = []
    User._id_counter = 1

    for entry in data:
        user = User.from_dict(entry)
        # maintain highest ID
        if user.id >= User._id_counter:
            User._id_counter = user.id + 1


def load_projects():
    """Load project dictionaries from JSON and rebuild Project instances."""
    data = load_json(PROJECTS_FILE)

    Project._projects = []
    Project._id_counter = 1

    for entry in data:
        project = Project.from_dict(entry)
        if project.id >= Project._id_counter:
            Project._id_counter = project.id + 1


def load_tasks():
    """Load task dictionaries from JSON and rebuild Task instances."""
    data = load_json(TASKS_FILE)

    Task._tasks = []
    Task._id_counter = 1

    for entry in data:
        task = Task.from_dict(entry)
        if task.id >= Task._id_counter:
            Task._id_counter = task.id + 1


def load_all():
    """Convenience helper to load everything in the correct order."""
    load_users()
    load_projects()
    load_tasks()
