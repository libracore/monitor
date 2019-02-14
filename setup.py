# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# get version from __version__ variable in monitor/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('monitor/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
	name='monitor',
	version=version,
	description='Environmental monitor app',
	author='Libracore AG',
	author_email='lars.mueller@libracore.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
