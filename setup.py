# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from textwrap import fill

_description = """\
PyRGG is a user-friendly synthetic random graph generator that is written in Python and supports multiple graph file formats, such as DIMACS-Graph files.
It can generate graphs of various sizes and is specifically designed to create input files for a wide range of graph-based research applications, including testing,
benchmarking, and performance analysis of graph processing frameworks.
PyRGG is aimed at computer scientists who are studying graph algorithms and graph processing frameworks.
"""

PYRGG_DESCRIPTION = fill(_description, width=113)


def get_requires():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return PYRGG_DESCRIPTION.replace("\n", " ")


setup(
    name='pyrgg',
    packages=['pyrgg', 'pyrgg.engines'],
    version='1.5',
    description='Python Random Graph Generator',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='PyRGG Development Team',
    author_email='info@pyrgg.site',
    url='https://github.com/sepandhaghighi/pyrgg',
    download_url='https://github.com/sepandhaghighi/pyrgg/tarball/v1.5',
    keywords='random graph python3 python generator graph-process generator DIMACS JSON YAML Pickle CSV TSV WEL ASP TGF UCINET',
    project_urls={
        'Webpage': 'https://www.pyrgg.site',
        'Source': 'https://github.com/sepandhaghighi/pyrgg',
    },
    install_requires=get_requires(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'pyrgg = pyrgg.__main__:main',
        ]})
