from argparse import ArgumentParser
from . import main as run, operations

# args parser
def main():
    parser = ArgumentParser(prog="Viper", description="A yarn like Python Package Manager")

    parser.add_argument("operation", choices=operations.keys())

    parser.add_argument("package", nargs='*', help="What package?")

    args = parser.parse_args()

    run(args)

if __name__ == "__main__":
    main()