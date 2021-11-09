from os import chdir, path
from urllib.request import urlopen as req
from tempfile import gettempdir
from bs4 import BeautifulSoup
import tarfile


def get_latest_version(package: str):
    # loading
    print("fetching...", end="\r")
    try:
        marked_source = req(f"https://pypi.org/simple/{package}").read()

        package_list = BeautifulSoup(marked_source, "html.parser")

        only_source = filter(
            lambda a: a.text.endswith(".tar.gz"), package_list.findAll("a")
        )
        without_dev_label = filter(lambda a: "dev" not in a.text, only_source)

        in_order = sorted(list(without_dev_label), key=lambda i: i.text, reverse=True)

        # all founded:
        # [ print(i.text) for i in in_order ]

        package_name, package_version = in_order[0].text.split("-")

        latest = {
            "url": in_order[0]["href"],
            "name": package_name,
            "version": package_version,
            "dirname": package_name + "-" + package_version[:-7],
        }

        return latest

    except Exception:
        return None

    finally:
        print()


def dowload_remote(package_url: str, package_dirname: str):
    tmp_dir = gettempdir()

    chdir(tmp_dir)

    package_tar_stream = req(package_url)

    print("extracting...", end="\r")

    try:
        package_tar = tarfile.open(fileobj=package_tar_stream, mode="r|gz")

        package_tar.extractall()

        chdir(path.join(tmp_dir, package_dirname))

        with open('setup.py') as setup_script:
            exec(setup_script.read())
    
    except Exception:
        return None

    finally:
        print()
