import os
import os.path
import click
from pathlib import Path


def replace_in_file(filename, search, replace):
    with open(filename, "r") as file:
        filedata = file.read()
    filedata = filedata.replace(search, replace)
    with open(filename, "w") as file:
        file.write(filedata)


@click.command()
@click.option("--search", prompt="Search", default="applications_container")
@click.option("--replace", prompt="Replace", default="applications_container")
def _rename(search, replace):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if ".git" not in dirpath:
                full_path = os.path.join(dirpath, filename)
                new_path = full_path.replace(search, replace)[1:]
                try:
                    Path(dirpath.replace(search, replace)).mkdir(
                        parents=True, exist_ok=True
                    )
                except FileExistsError:
                    pass
                os.rename(os.getcwd() + full_path[1:], os.getcwd() + new_path)
                full_path = os.getcwd() + new_path
                try:
                    replace_in_file(full_path, search, replace)
                except UnicodeDecodeError:
                    pass


if __name__ == "__main__":
    _rename()
