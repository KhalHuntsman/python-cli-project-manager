#!/usr/bin/env python3
# Author
# Date: 12/9/25 
# Version 1.1

"""
Project model definition.

Represents a project owned by a specific User and containing multiple
Tasks. Includes class-level storage, ID generation, controlled attribute
access, relationship management, and JSON serialization helpers.
"""

from models.user import User


class Project:
    # Class-wide ID counter and storage list
    _id_counter = 1
    _projects = []

    def __init__(self, title: str, description: str, due_date: str, user_id: int):
        # Unique ID
        self.id = Project._id_counter
        Project._id_counter += 1

        # Controlled attributes
        self.title = title
        self.description = description
        self.due_date = due_date

        # Link to user
        self.user_id = user_id
        self.tasks = []  # one-to-many relationship: Project → Tasks

        # Add project to user (if user exists)
        user = User.get_by_id(user_id)
        if user:
            user.add_project(self)

        # Store this instance in the class-level list
        Project._projects.append(self)

    # -------------------- PROPERTIES --------------------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Project title must be a non-empty string.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise ValueError("Project description must be a string.")
        self._description = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Due date must be provided as a string.")
        self._due_date = value

    # -------------------- RELATIONSHIP METHODS --------------------
    def add_task(self, task):
        """Attach a new Task to this project."""
        self.tasks.append(task)

    # -------------------- SERIALIZATION --------------------
    def to_dict(self):
        """Convert this project into a serializable dict."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id,
            "tasks": [t.id for t in self.tasks],
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a Project instance from stored data."""
        project = cls(
            data["title"],
            data["description"],
            data["due_date"],
            data["user_id"]
        )
        project.id = data["id"]  # keep original ID
        return project

    # -------------------- CLASS METHODS --------------------
    @classmethod
    def get_all(cls):
        return cls._projects

    @classmethod
    def get_by_id(cls, project_id: int):
        return next((p for p in cls._projects if p.id == project_id), None)

    @classmethod
    def create(cls, title, description, due_date, user_id):
        return cls(title, description, due_date, user_id)

    # -------------------- STRING REPRESENTATION --------------------
    def __repr__(self):
        return (
            f"Project(id={self.id}, title='{self.title}', "
            f"user_id={self.user_id}, due='{self.due_date}')"
        )
