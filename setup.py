# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from textwrap import fill

_description = """\
Pyrgg is an easy-to-use synthetic random graph generator written in Python
which supports various graph file formats including DIMACS .gr files.
Pyrgg has the ability to generate graphs of different sizes
and is designed to provide input files
for broad range of graph-based research applications,
including but not limited to testing,
benchmarking and performance-analysis of graph processing frameworks.
Pyrgg target audiences are computer scientists
who study graph algorithms and graph processing frameworks.
"""

PYRGG_DESCRIPTION = fill(_description, width=70)


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
    packages=['pyrgg'],
    version='1.4',
    description='Python Random Graph Generator',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='PyRGG Development Team',
    author_email='info@pyrgg.ir',
    url='https://github.com/sepandhaghighi/pyrgg',
    download_url='https://github.com/sepandhaghighi/pyrgg/tarball/v1.4',
    keywords='random graph python3 python generator graph-process generator DIMACS JSON YAML Pickle CSV TSV WEL ASP TGF UCINET',
    project_urls={
        'Webpage': 'https://www.pyrgg.ir',
        'Source': 'https://github.com/sepandhaghighi/pyrgg',
    },
    install_requires=get_requires(),
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
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
