try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="foo",
    version="0.0.1",
    description="Test python module",
    author="Brendon Jones",
    author_email="brendonj@waikato.ac.nz",
    url="http://www.wand.net.nz",
    packages=["foo"],
    package_dir = {
        "foo":"foo",
        },
    )
