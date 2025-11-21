#!/usr/bin/env python
import subprocess
import sys
import os

ENV_NAME = "yolo-fine"
PYTHON_VERSION = "3.10"
REQUIREMENTS_FILE = "requirements.txt"

def run_command(command, check_error=True):
    """Executes a shell command and prints output."""
    print(f"\n---> Executing: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            check=check_error,
            text=True,
            capture_output=True
        )
        print(result.stdout)
        if result.stderr:
            print("--- Standard Error ---")
            print(result.stderr)
        return result
    except FileNotFoundError:
        print(f"Error: The command '{command[0]}' was not found.")
        print("Please ensure conda is installed and accessible in your system's PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with exit code {e.returncode}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

def environment_exists(env_name):
    """Checks if a conda environment exists."""
    command = ["conda", "info", "--envs"]
    result = subprocess.run(command, text=True, capture_output=True)
    
    if any(line.strip().startswith(env_name) for line in result.stdout.splitlines()):
         return True
    return False

def setup_environment():
    """Automates the creation (if needed) and setup of the conda environment."""
    
    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"Error: '{REQUIREMENTS_FILE}' not found. Please create this file.")
        sys.exit(1)

    if environment_exists(ENV_NAME):
        print(f"Environment '{ENV_NAME}' already exists. Skipping creation.")
    else:
        print(f"Environment '{ENV_NAME}' not found. Creating a new one...")
        create_command = ["conda", "create", "--name", ENV_NAME, f"python={PYTHON_VERSION}", "--yes"]
        run_command(create_command)

    print(f"\nUpdating packages in '{ENV_NAME}' based on {REQUIREMENTS_FILE}...")
    
    install_uv_command = [
        "conda", "run", "-n", ENV_NAME,
        "pip", "install", "uv"
    ]
    run_command(install_uv_command)

    install_deps_command = [
        "conda", "run", "-n", ENV_NAME,
        "uv", "pip", "install", "-r", REQUIREMENTS_FILE
    ]
    run_command(install_deps_command)

    print("\n==============================================")
    print(f"Conda environment '{ENV_NAME}' is ready and up-to-date.")
    print(f"Next step: Activate the environment using: conda activate {ENV_NAME}")
    print("==============================================")

if __name__ == "__main__":
    setup_environment()
