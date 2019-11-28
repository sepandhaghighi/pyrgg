# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


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
        return '''Pyrgg is an easy-to-use synthetic random graph generator written in Python which supports various
                   graph file formats including DIMACS .gr files. Pyrgg has the ability to generate graphs of different
                   sizes and is designed to provide input files for broad range of graph-based research applications,
                   including but not limited to testing, benchmarking and performance-analysis of graph processing frameworks.
                   Pyrgg target audiences are computer scientists who study graph algorithms and graph processing frameworks.'''


setup(
    name='pyrgg',
    packages=['pyrgg'],
    version='0.3',
    description='Python Random Graph Generator',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Sepand Haghighi',
    author_email='sepand@qpage.ir',
    url='https://github.com/sepandhaghighi/pyrgg',
    download_url='https://github.com/sepandhaghighi/pyrgg/tarball/v0.3',
    keywords='random graph python3 python generator graph-process generator DIMACS JSON YAML Pickle CSV WEL ASP TGF UCINET',
    install_requires=get_requires(),
    python_requires='>=3.4',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
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
)
