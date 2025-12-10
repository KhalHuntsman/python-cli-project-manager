#!/usr/bin/env python3
# Author
# Date: 12/9/25 
# Version 1.1

"""
Task model definition.

Represents a unit of work within a Project. Includes class-level storage,
ID generation, controlled attribute access, relationship management,
task completion tracking, and JSON serialization helpers.
"""

from models.project import Project


class Task:
    # Class-level ID tracking and storage
    _id_counter = 1
    _tasks = []

    def __init__(self, title: str, assigned_to: str, project_id: int, status: str = "pending"):
        # Unique ID
        self.id = Task._id_counter
        Task._id_counter += 1

        # Controlled attributes
        self.title = title
        self.assigned_to = assigned_to
        self.status = status  # "pending" or "completed"

        # Relationship: belongs to a project
        self.project_id = project_id
        project = Project.get_by_id(project_id)
        if project:
            project.add_task(self)

        # Store instance in class-level list
        Task._tasks.append(self)

    # -------------------- PROPERTIES --------------------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Task title must be a non-empty string.")
        self._title = value

    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("assigned_to must be a non-empty string.")
        self._assigned_to = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed = ["pending", "completed"]
        if value not in allowed:
            raise ValueError("Status must be 'pending' or 'completed'.")
        self._status = value

    # -------------------- BEHAVIOR METHODS --------------------
    def mark_complete(self):
        """Mark this task as completed."""
        self.status = "completed"

    # -------------------- SERIALIZATION --------------------
    def to_dict(self):
        """Convert task into a dictionary for JSON saving."""
        return {
            "id": self.id,
            "title": self.title,
            "assigned_to": self.assigned_to,
            "status": self.status,
            "project_id": self.project_id,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a Task object from stored data."""
        task = cls(
            data["title"],
            data["assigned_to"],
            data["project_id"],
            status=data["status"],
        )
        task.id = data["id"]
        return task

    # -------------------- CLASS METHODS --------------------
    @classmethod
    def get_all(cls):
        return cls._tasks

    @classmethod
    def get_by_id(cls, task_id: int):
        return next((t for t in cls._tasks if t.id == task_id), None)

    @classmethod
    def create(cls, title, assigned_to, project_id):
        return cls(title, assigned_to, project_id)

    # -------------------- STRING REPRESENTATION --------------------
    def __repr__(self):
        return (
            f"Task(id={self.id}, title='{self.title}', "
            f"status='{self.status}', project_id={self.project_id})"
        )
