import os
import yaml


def main(args: list[str]):
    user_location = os.getcwd()
    project_yaml_path = os.path.join(user_location, "package.yaml")

    if os.path.isfile(project_yaml_path):
        print("there is a package.yaml here already... aborting")
        return

    project_name = input("Name of project: ") if len(args) == 0 else args[0]
    user_name = os.environ["USER"] or input("What is your name? ")

    project_dict = mount_project_dictonary(project_name, user_name)
    project_yaml = yaml.dump(project_dict, sort_keys=False)

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


def mount_project_dictonary(name, author):
    # todo: regex
    return {"name": name, "author": author}
