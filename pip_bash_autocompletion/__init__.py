import sys
import os

BASH_COMPLETION_DIR = os.path.expanduser('~/bash_completion.d')
BASH_COMPLETION_SOURCE = """
if [ -d {0} ]; then
    . {0}/*
fi
""".format(BASH_COMPLETION_DIR)


try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

AUTOCOMPLETE = """
_pip() {
     local cur prev opts
     COMPREPLY=()
     cur="${COMP_WORDS[COMP_CWORD]}"
     prev="${COMP_WORDS[COMP_CWORD-1]}"
     if [[ ${prev} == 'install' ]] ; then
         COMPREPLY=( $( grep ^$cur ~/.pip_index ) )
         return 0
     fi

 }
_pip_upgrade() {
     local cur prev opts
     COMPREPLY=()
     cur="${COMP_WORDS[COMP_CWORD]}"
     COMPREPLY=( $( grep ^$cur ~/.pip_index ) )
     return 0

 }
 complete -F _pip pip pip2 pip3
 complete -F _pip_upgrade pip_upgrade
 """


def update():
    sys.stderr.write("\nConnecting to pypi...\n")
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    index_file_name = os.path.expanduser('~/.pip_index')

    sys.stderr.write("Opening index file...\n")
    with open(index_file_name, 'w') as index_file:
        sys.stderr.write("Retrieving package list...\n")
        packages = client.list_packages()
        sys.stderr.write("Writing package cache...\n")
        index_file.write('\n'.join(packages))
    sys.stderr.write("Updated cache!\n")


def install():
    sys.stderr.write("\n")

    if not os.path.exists(BASH_COMPLETION_DIR):
        sys.stderr.write("Creating {0}...\n".format(BASH_COMPLETION_DIR))
        os.makedirs(BASH_COMPLETION_DIR)

    destination_name = os.path.join(BASH_COMPLETION_DIR, 'pip')
    sys.stderr.write("Writing {0}...\n".format(destination_name))
    open(destination_name, 'w').write(AUTOCOMPLETE)

    sys.stderr.write("Looking for entry in ~/.bashrc...\n")
    profile_file_name = os.path.expanduser('~/.bashrc')
    with open(profile_file_name) as profile_file:
        installed = (BASH_COMPLETION_SOURCE in profile_file.read())

    if installed:
        sys.stderr.write("Found entry in in ~/.bashrc...\n")
    else:
        with open(profile_file_name, 'a') as profile_file:
            sys.stderr.write("Appending entry to ~/.bashrc...\n")
            profile_file.write(BASH_COMPLETION_SOURCE)

    sys.stderr.write("Installed bash completion!\n")