#!/usr/bin/env python3

# Author
# Date: 12/9/25
# Version 1.1

"""
Basic tests for CLI behavior.
"""

import subprocess
import sys
import os

def run_cli(args):
    """Helper to run the CLI command in a subprocess."""
    cmd = [sys.executable, "main.py"] + args
    return subprocess.run(cmd, capture_output=True, text=True)


def test_cli_add_user():
    result = run_cli(["add-user", "--name", "TestUser", "--email", "test@example.com"])
    assert result.returncode == 0
    assert "User created" in result.stdout


def test_cli_list_users():
    result = run_cli(["list-users"])
    assert result.returncode == 0
