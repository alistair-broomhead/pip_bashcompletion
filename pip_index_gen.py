try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib
client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')
packages = client.list_packages()
for package in packages:
    print(package)

