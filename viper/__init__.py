from argparse import Namespace

from .init import main as __init
from .install import main as __install
from .remove import main as __remove

operations = {
    "install": __install,
    "remove": __remove,
    "init": __init,
}

def main(args: Namespace):
    operation = args.operation
    package = args.package
    operations[operation](package)
