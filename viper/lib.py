import os
import subprocess
import yaml


def write_project_yaml(name, author):
    # todo: regex to validate fields
    project_dict = {
        "name": name,
        "version": "1.0.0",
        "main": f"{name}/__init__.py",
        "author": author,
        "license": "MIT",
        "tasks": {
            "start": f"venv/bin/python {name}/__init__.py",
        },
    }

    return yaml.dump(
        project_dict,
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
    package_file = os.path.join(os.getcwd(), "package.yaml")
    pip_file = os.path.join(os.getcwd(), "venv", "bin", "pip")
    python_file = os.path.join(os.getcwd(), "venv", "bin", "python")
    activate_file = os.path.join(os.getcwd(), "venv", "bin", "activate")

    for req_file in [package_file, pip_file, python_file, activate_file]:
        if not os.path.isfile(req_file):
            raise Exception("Not in a Viper Project Root!")

    os.system(f"source {activate_file}")

    subprocess.call(f". {activate_file}", shell=True)

    with open(package_file, "+r") as file:
        return yaml.load(file, Loader=yaml.FullLoader)
