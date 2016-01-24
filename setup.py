#!/usr/bin/env python
info="""
<<<<<<< HEAD
Allow use of system vtk from a virtualenv
Should work on all platforms.

=======
Allow use of system Wx from a virtualenv
Should work on all platforms.

Qt support is currently experimental.

>>>>>>> 20073707247148f6bb5f789945edd811d12e814c
report bugs to https://github.com/stuaxo/vext
"""

version="0.5.11"
vext_version="vext>=%s" % version


from glob import glob
from subprocess import call

from setuptools import setup
from setuptools.command.install import install
from setuptools.command.install_lib import install_lib

import sys

vext_files = glob("*.vext")

def _post_install(self):
    cmd = ["vext", "-e", "-i" + (" -i".join(vext_files))]
    call(cmd)

class Install(install):
    def run(self):
        # from pip
        #
        # if ran from some setup.py then vexts own setup will take care of this...
        #
        # TOOD - Move this code to a common place.
<<<<<<< HEAD
        print("vext.vtk Install")
=======
        print("vext.gi Install")
>>>>>>> 20073707247148f6bb5f789945edd811d12e814c
        if sys.prefix == '/usr':
            print "Not installing PTH file to real prefix"
            return
        call(["pip", "install", vext_version])
        self.do_egg_install()
        self.execute(_post_install, [self], msg="Install vext files:")

setup(
<<<<<<< HEAD
    name='vext.vtk',
    zip_safe=False,

    cmdclass={
          'install': Install,
=======
    name='vext.wx',
    version=version,
    description='Use system wx from a virtualenv',
    long_description=info,

    cmdclass={
        'install': Install,
>>>>>>> 20073707247148f6bb5f789945edd811d12e814c
    },

    version=version,

    description='Use system python packages in a virtualenv',
    long_description=info,

    # The project's main homepage.
    url='https://github.com/stuaxo/vext',

    # Author details
    author='Stuart Axon',
    author_email='stuaxo2@yahoo.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    # What does your project relate to?
    keywords='virtualenv vext vtk',

<<<<<<< HEAD
    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    setup_requires=[vext_version, "setuptools>=0.18.8"],
    install_requires=[vext_version],
    data_files=[('', vext_files)]
=======
    setup_requires=["setuptools>=0.18.8"],
    install_requires=[vext_version],
>>>>>>> 20073707247148f6bb5f789945edd811d12e814c
)
