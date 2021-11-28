from argparse import Namespace
from datetime import datetime

from .actions import add, remove, init, run

operations = {
    "init": init,
    "run": run,
    "add": add,
    "remove": remove,
}

def main(args: Namespace):
    started_at = datetime.now()

    operation = args.operation
    package = args.package

    print(f'⏳ viper {operation}')
    
    operations[operation](package)

    done_in = datetime.now() - started_at
    print("⌛ Done in:", str(done_in.seconds) + "s")
