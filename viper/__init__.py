from argparse import Namespace

from .init import main as __init
from .install import main as __install
from .remove import main as __remove


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
