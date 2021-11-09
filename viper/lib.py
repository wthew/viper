import os
import subprocess
from typing import Union
import yaml


def write_project_yaml(name, author):
    # todo: regex to validate fields

    return yaml.dump(
        {
            "name": name,
            "version": "1.0.0",
            "main": f"{name}/__init__.py",
            "author": author,
            "license": "MIT",
            "tasks": {
                "start": f"venv/bin/python {name}/__init__.py",
            },
        },
        sort_keys=False,
        indent=4,
    )


def read_project_yaml():
    user_location = os.getcwd()
    project_yaml_path = os.path.join(user_location, "package.yaml")

    if not os.path.isfile(project_yaml_path):
        print("you not in any viper project")
        return

    with open(project_yaml_path, "+r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def check_project():
    NoProjectError = Exception("Not in a Viper Project Root!")

    package_file = os.path.join(os.getcwd(), "package.yaml")
    pip_file = os.path.join(os.getcwd(), "venv", "bin", "pip")
    python_file = os.path.join(os.getcwd(), "venv", "bin", "python")
    activate_file = os.path.join(os.getcwd(), "venv", "bin", "activate")

    if not os.path.isfile(package_file):
        raise NoProjectError

    if not os.path.isfile(pip_file):
        raise NoProjectError
    
    if not os.path.isfile(python_file):
        raise NoProjectError
    
    if not os.path.isfile(activate_file):
        raise NoProjectError
    
    subprocess.call(f". {activate_file}", shell=True)

    with open(package_file, "+r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)