#!/usr/bin/env python3
# Author: Hunter Steele
# Date: 12/9/25 
# Version: 1.1

"""
General helper functions for validation and lookup utilities used by the CLI.

These helper functions keep the codebase clean and avoid duplication.
"""

from models.user import User
from models.project import Project


def find_user_or_error(user_id, console):
    """
    Return a User if found.

    Otherwise print an error to the provided console and return None.
    """
    user = User.get_by_id(user_id)
    if not user:
        console.print(f"[bold red]Error: No user found with ID {user_id}[/]")
        return None
    return user


def find_project_or_error(project_id, console):
    """
    Return a Project if found.

    Otherwise print an error to the provided console and return None.
    """
    project = Project.get_by_id(project_id)
    if not project:
        console.print(f"[bold red]Error: No project found with ID {project_id}[/]")
        return None
    return project


def validate_nonempty(value, field_name):
    """
    Simple reusable validation helper.

    Raises ValueError if the value is empty; otherwise returns the value.
    """
    if not value:
        raise ValueError(f"{field_name} cannot be empty")
    return value
