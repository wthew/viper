import os
from pip._internal.operations import install
from pip._internal.operations.freeze import freeze

from viper.utils import dowload_remote, get_latest_version
from .lib import (
    check_project,
    read_project_yaml,
    write_project_yaml,
)


def init(args: list[str]):
    user_location = os.getcwd()
    project_yaml_path = os.path.join(user_location, "package.yaml")

    if os.path.isfile(project_yaml_path):
        print("there is a package.yaml here already... aborting")
        return

    project_name = input("Name of project: ") if len(args) == 0 else args[0]
    user_name = os.environ["USER"] or input("What is your name? ")

    project_yaml = write_project_yaml(project_name, user_name)

    print(f"\n🔧 Making {project_name}, an awesome project, in", user_location)

    os.mkdir(project_name)
    os.chdir(project_name)

    with open("package.yaml", "+w") as file:
        file.write(project_yaml)

    print("\n🐍 creating venv...", end="\r")

    os.system("python -m venv venv")

    print("🐍 creating venv... created!")

    print("\nMaking initials files...")

    os.mkdir(project_name)
    os.system(f"touch {project_name}/__init__.py")

    print("\n🐙 creating git local repo...")
    os.system("git init")
    os.system('echo "venv" >> .gitignore')

    print(f"\n✨ Done. now, open with: `code {project_name}`")


def run(args: list[str]):
    task = args[0]

    os.system("source venv/bin/activate")

    properties = read_project_yaml()

    if properties is None:
        print("Error.")
        return

    tasks = properties["tasks"]

    if task in tasks:
        os.system(tasks[task])

    else:
        print(f"not exist task {task} in package")


def add(args: list[str]):
    check_project()

    print(args)

    latest = get_latest_version(args[0])

    if latest:
        dowload_remote(latest["url"], latest["dirname"])

    else:
        print("404")


def remove(args: list[str]):
    print("removenf", args)
