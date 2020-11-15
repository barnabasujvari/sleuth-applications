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
            filereplace(os.path.join(dirpath, filename),search,replace)
            print()