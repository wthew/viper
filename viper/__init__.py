from argparse import Namespace

from .init import main as __init
from .install import main as __install
from .remove import main as __remove


operations = {
    "install": lambda pos_args: __install(pos_args),
    "remove": lambda pos_args: __remove(pos_args),
    "init": lambda pos_args: __init(pos_args),
}


def main(args: Namespace):
    operation = args.operation
    package = args.package
    operations[operation](package)
