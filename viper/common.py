import yaml

sample = """
name: Viper
version: 1.0.0
main: __main__.py
author: wthew <wellingtondeferreiraqueiroz@gmail.com>
license: MIT

tasks:
  - start: echo 'starting'
  - build: echo 'building'
  - dev: echo 'deving'

requires:
  - argparse
  - yaml

dependencies:
  - click: 8.0.1
  - mypy-extensions: 0.4.3
  - pathspec: 0.9.0
  - platformdirs: 2.3.0
  - pycodestyle: 2.7.0
  - regex: 2021.8.28
  - toml: 0.10.2
  - tomli: 1.2.1
  - typing-extensions: 3.10.0.2
"""

def parser_file(file):
    print(file)
    parsed = yaml.load(sample)

    print(f'{parsed=}')
