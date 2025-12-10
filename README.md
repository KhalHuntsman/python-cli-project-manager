# Python CLI Project Manager

A command-line application for managing **Users**, **Projects**, and **Tasks** using Python, JSON-based persistence, and object-oriented design.  
Built as part of a course module focusing on OOP principles, CLI development, file I/O, testing, and structured project organization.

---

## Features

### Object-Oriented Design
- Separate `User`, `Project`, and `Task` classes.
- One-to-many relationships:
  - **User → Projects**
  - **Project → Tasks**
- Class-level ID tracking, properties with validation, serialization helpers, and relationship methods.

### Command-Line Interface (argparse)
Supports the following commands:

| Command | Description |
|--------|-------------|
| `add-user` | Create a new user |
| `list-users` | List all users |
| `add-project` | Create a project for a specific user |
| `list-projects` | List all projects |
| `add-task` | Add a task to a project |
| `list-tasks` | List all tasks |
| `complete-task` | Mark a task as completed |

### JSON Persistence
All Users, Projects, and Tasks persist across runs using JSON files stored in the `data/` directory.  
The program automatically loads JSON on startup and saves changes after every command.

### External Package: Rich
The CLI uses the **Rich** library to render tables with clean formatting.

Install with:
- pip install rich

### Testing (pytest)
Includes unit tests for:
- User model  
- Project model  
- Task model  
- Basic CLI execution  

Tests are located in the `tests/` directory.

---

## Project Structure
cli_manager/
│
├── main.py # CLI entry point
│
├── models/
│ ├── user.py # User class
│ ├── project.py # Project class
│ └── task.py # Task class
│
├── utils/
│ └── storage.py # JSON load/save helpers
│
├── data/
│ ├── users.json # Auto-generated
│ ├── projects.json
│ └── tasks.json
│
├── tests/
│ ├── test_users.py
│ ├── test_projects.py
│ ├── test_tasks.py
│ └── test_cli.py
│
└── README.md

This organization separates concerns cleanly and improves maintainability.

---

## Running the Program

### 1. Install Dependencies
pip install rich

### 2. Run a Command
General format:

python main.py <command> [options]

##  Example Commands

### Create a User
python main.py add-user --name "Alex" --email "alex@example.com"

### List Users
python main.py list-users

### Create a Project
python main.py add-project --title "CLI App" --description "Course project" --due "2025-12-31" --user-id 1

### Add a Task
python main.py add-task --title "Write CLI" --assigned-to "Alex" --project-id 1

### Mark a Task Complete
python main.py complete-task --task-id 1

---

## Development Notes

- The program loads all data from JSON at startup using `load_all()`.
- After every command, `save_all()` writes updated data back to disk.
- Each model handles its own ID assignment and relationship tracking.
- Tests are run with pytest

---

## General project notes:
This project completed with assistance of ChatGPT to suggest solutions, find and point out syntax and spelling errors, and create inline commentary as well as the README.md document. All ChatGPT output was reviewed for accuracy and understanding before submission.

#### Author: Hunter Steele
#### Date: 12/9/25
#### Version 1.1