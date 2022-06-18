import os, sys, subprocess

from viper.lib import (
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

    if task not in tasks:
        print(f"not exist task {task} in package")
        return
    
    here = os.getcwd()
    project_root = os.path.join(here, properties["name"])
    print(f'{project_root=}')
    sys.path.append(project_root)
    sys.path.append(os.path.dirname(project_root))
    os.environ['PATH'] += os.pathsep + os.path.abspath(project_root)
    os.environ['PATH'] += os.pathsep + os.path.abspath(os.path.dirname(project_root))

    if here in sys.path:
        sys.path.remove(here)

    print(f'{os.environ["PATH"]=}')
    subprocess.run(tasks[task], shell=True, env=os.environ, cwd=here)

def add(args: list[str]):
    project = check_project()

    python_file = os.path.join(os.getcwd(), "venv", "bin", "python")

    packages = " ".join(args)
    os.system(f"{python_file} -m pip install {packages}")
    os.system(f"{python_file} -m pip freeze > requirements.txt")


def remove(args: list[str]):
    print("removenf", args)
