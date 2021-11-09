from setuptools import setup, find_packages

setup(
    name="viper",
    version="1.0.0",
    description="A Yarn like Python Package Manager",
    author="wthew",
    url="https://github.com/wthew/viper",
    install_requires=["pyyaml", "bs4"],
    packages=find_packages(where="."),
    python_requires=">=3.6, <4",
)
