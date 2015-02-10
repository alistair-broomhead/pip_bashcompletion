import sys
import os

try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

AUTOCOMPLETE = """_pip() {
     local cur prev opts
     COMPREPLY=()
     cur="${COMP_WORDS[COMP_CWORD]}"
     prev="${COMP_WORDS[COMP_CWORD-1]}"
     if [[ ${prev} == 'install' ]] ; then
         COMPREPLY=( $( grep ^$cur ~/.pip_index ) )
         return 0
     fi

 }
 complete -F _pip pip"""


def update():
    sys.stderr.write("\nConnecting to pypi...\n")
    client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
    index_file_name = os.path.expanduser('~/.pip_index')
    sys.stderr.write("Opening index file...\n")
    with open(index_file_name, 'w') as index_file:
        sys.stderr.write("Retrieving package list...\n")
        packages = client.list_packages()
        index_file.writelines(packages)
    sys.stderr.write("Done!\n")


def install():
    destination_dir = os.path.expanduser('~/bash_completion.d')

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    destination_name = os.path.join(destination_dir, 'pip')
    open(destination_name, 'w').write(AUTOCOMPLETE)