#!/usr/bin/env python3
# Author
# Date: 12/9/25 
# Version 1.1

"""
User model definition.

Represents a system user who owns one or more projects. Includes
class-level collections, controlled attribute access, ID generation,
relationship management, and JSON serialization helpers.
"""

class User:
    # Class-level attributes for ID generation and storage
    _id_counter = 1
    _users = []

    def __init__(self, name: str, email: str):
        # Assign unique ID from class counter
        self.id = User._id_counter
        User._id_counter += 1

        # Controlled attributes using property setters
        self.name = name
        self.email = email

        # A user can have many projects (relationship: 1-to-many)
        self.projects = []

        # Store instance in class-level list
        User._users.append(self)

    # -------------------- PROPERTIES --------------------
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("User name must be a non-empty string.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email format.")
        self._email = value

    # -------------------- RELATIONSHIP METHODS --------------------
    def add_project(self, project):
        """Attach a project to this user."""
        self.projects.append(project)

    # -------------------- SERIALIZATION --------------------
    def to_dict(self):
        """Convert this User into a dictionary for JSON saving."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.id for p in self.projects]
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Reconstruct a User instance from saved dictionary data."""
        user = cls(data["name"], data["email"])
        user.id = data["id"]  # restore original ID
        return user

    # -------------------- CLASS METHODS --------------------
    @classmethod
    def get_all(cls):
        return cls._users

    @classmethod
    def get_by_id(cls, user_id: int):
        return next((u for u in cls._users if u.id == user_id), None)

    @classmethod
    def create(cls, name, email):
        """Factory method to create a User and return it immediately."""
        return cls(name, email)

    # -------------------- STRING REPRESENTATION --------------------
    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"
