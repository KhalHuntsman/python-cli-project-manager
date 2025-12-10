#!/usr/bin/env python3

# Author
# Date: 12/9/25
# Version 1.1
 
"""
CLI entry point for the User/Project/Task management system.

Provides commands for creating and listing Users, Projects, and Tasks,
as well as marking tasks as completed. Uses argparse for command-line
parsing, Rich for formatted output, and JSON utilities for persistence.
"""

import argparse
from rich.table import Table
from rich.console import Console

from models.user import User
from models.project import Project
from models.task import Task
from utils.storage import load_all, save_all


console = Console()


# -------------------- HELPER FUNCTIONS (DISPLAY) --------------------
def show_users():
    table = Table(title="Users")
    table.add_column("ID", justify="right")
    table.add_column("Name")
    table.add_column("Email")
    table.add_column("Projects")

    for u in User.get_all():
        table.add_row(str(u.id), u.name, u.email, str(len(u.projects)))

    console.print(table)


def show_projects():
    table = Table(title="Projects")
    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("User ID")
    table.add_column("Due Date")
    table.add_column("Tasks")

    for p in Project.get_all():
        table.add_row(str(p.id), p.title, str(p.user_id), p.due_date, str(len(p.tasks)))

    console.print(table)


def show_tasks():
    table = Table(title="Tasks")
    table.add_column("ID", justify="right")
    table.add_column("Title")
    table.add_column("Assigned To")
    table.add_column("Status")
    table.add_column("Project ID")

    for t in Task.get_all():
        table.add_row(
            str(t.id), t.title, t.assigned_to, t.status, str(t.project_id)
        )

    console.print(table)


# -------------------- COMMAND FUNCTIONS --------------------
def command_add_user(args):
    User.create(args.name, args.email)
    save_all()
    console.print(f"[bold green]User created:[/] {args.name}")


def command_list_users(args):
    show_users()


def command_add_project(args):
    user = User.get_by_id(args.user_id)
    if not user:
        console.print("[bold red]Error: User not found.[/]")
        return

    Project.create(args.title, args.description, args.due, args.user_id)
    save_all()
    console.print(f"[bold green]Project created:[/] {args.title}")


def command_list_projects(args):
    show_projects()


def command_add_task(args):
    project = Project.get_by_id(args.project_id)
    if not project:
        console.print("[bold red]Error: Project not found.[/]")
        return

    Task.create(args.title, args.assigned_to, args.project_id)
    save_all()
    console.print(f"[bold green]Task created:[/] {args.title}")


def command_list_tasks(args):
    show_tasks()


def command_complete_task(args):
    task = Task.get_by_id(args.task_id)
    if not task:
        console.print("[bold red]Error: Task not found.[/]")
        return

    task.mark_complete()
    save_all()
    console.print(f"[bold green]Task marked complete:[/] {task.title}")


# -------------------- MAIN CLI SETUP --------------------
def build_parser():
    parser = argparse.ArgumentParser(
        description="User/Project/Task Management CLI"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- USERS ----
    add_user = subparsers.add_parser("add-user", help="Create a new user")
    add_user.add_argument("--name", required=True)
    add_user.add_argument("--email", required=True)
    add_user.set_defaults(func=command_add_user)

    list_users = subparsers.add_parser("list-users", help="List all users")
    list_users.set_defaults(func=command_list_users)

    # ---- PROJECTS ----
    add_project = subparsers.add_parser("add-project", help="Create a new project")
    add_project.add_argument("--title", required=True)
    add_project.add_argument("--description", required=True)
    add_project.add_argument("--due", required=True)
    add_project.add_argument("--user-id", type=int, required=True)
    add_project.set_defaults(func=command_add_project)

    list_projects = subparsers.add_parser("list-projects", help="List all projects")
    list_projects.set_defaults(func=command_list_projects)

    # ---- TASKS ----
    add_task = subparsers.add_parser("add-task", help="Create a new task")
    add_task.add_argument("--title", required=True)
    add_task.add_argument("--assigned-to", required=True)
    add_task.add_argument("--project-id", type=int, required=True)
    add_task.set_defaults(func=command_add_task)

    list_tasks = subparsers.add_parser("list-tasks", help="List all tasks")
    list_tasks.set_defaults(func=command_list_tasks)

    complete_task = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_task.add_argument("--task-id", type=int, required=True)
    complete_task.set_defaults(func=command_complete_task)

    return parser


def main():
    # Load existing JSON data on startup
    load_all()

    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
