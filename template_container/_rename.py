import os
import os.path
from pyutil import filereplace
import click

@click.command()
@click.option('--search',  prompt='Search', default="template_container")
@click.option('--replace',  prompt='Replace', default="template_container")
def _rename(search, replace):
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            filereplace(full_path,search,replace)
            os.rename(full_path,full_path.replace(search,replace))