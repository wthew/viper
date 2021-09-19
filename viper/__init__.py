from argparse import Namespace


def __install(package_name: str):
    print("installing", package_name)
    pass


def __remove(package_name: str):
    print("removing", package_name)
    pass


def __init():
    print("init a project")
    pass


operations = {
    "install": lambda package: __install(package),
    "remove": lambda package: __remove(package),
    "init": lambda: __init(),
}


def main(args: Namespace):
    operation = args.operation
    package = args.package

    print("main...")
    operations[operation](package)
