import os
import yaml


def main(args: list[str]):
    user_location = os.getcwd()
    user_name = os.environ["USER"]
    project_yaml_path = os.path.join(user_location, "package.yaml")

    print("\ninit a project in", user_location)

    if os.path.isfile(project_yaml_path):
        print("there is a package.yaml... aborting")
        return

    project_name = input("Name of project: ") if len(args) == 0 else args[0]

    project_dict = mount_project_dictonary(project_name, user_name)
    project_yaml = yaml.dump(project_dict)


def mount_project_dictonary(name, author):
    # todo: regex
    return {"name": name, "author": author}
