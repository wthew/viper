from argparse import ArgumentParser
from .viper import main, operations

# args parser

parser = ArgumentParser(prog="Viper", description="A yarn like Python Package Manager")

parser.add_argument("operation", choices=operations.keys())

parser.add_argument("package", help="What package?")

args = parser.parse_args()

main(args)
