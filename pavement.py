import re
import os
from functools import partial

from paver import doctools
from paver.easy import options, Bunch, task, sh
from paver.path25 import path, pushd

options(
    sphinx=Bunch(
        builddir='_build',
    )
)

def read_requirements(filename):
    """
    Read pip requirements file and return it's canonical form in a string
    -- without unnecessary whitespace, comments and sorted alphabetically.
    """
    strip_whitespace = partial(map, str.strip)
    remove_empty_lines = partial(filter, None)
    strip_comments = partial(filter, lambda line: not line.startswith('#'))
    return (
        '\n'.join(
        sorted(
        strip_comments(
        remove_empty_lines(
        strip_whitespace(
        open(filename)))))))


@task
def install_dependencies():
    """
    Installs required python packages.

    Only install if the requirements file changed.
    """
    requirements_file = 'requirements.txt'
    installed_file = 'requirements.installed'
    requirements = read_requirements(requirements_file)
    installed = os.path.exists(installed_file) and open(installed_file).read()
    if installed == requirements:
        print ('Nothing new to install. Delete %s if you want to try anyway' %
            installed_file)
    else:
        sh('pip install -r ' + requirements_file)

        # remember what was installed
        with open(installed_file, 'w+') as f:
            f.write(requirements)
    

@task
def delete_pyc():
    """
    Delete all *.pyc files recursively from this directory.
    """
    for file in path('.').walkfiles('*.pyc'):
        file.remove()

@task
def build_docs():
    doctools.doc_clean()
    doctools.html()