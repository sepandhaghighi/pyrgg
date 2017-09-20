from distutils.core import setup
setup(
  name = 'pyrgg',
  packages = ['pyrgg'],
  version = '0.2',
  description = 'Python Random Graph Generator',
  long_description='''Pyrgg is an easy-to-use synthetic random graph generator written in Python which supports various
                   graph file formats including DIMACS .gr files. Pyrgg has the ability to generate graphs of different
                   sizes and is designed to provide input files for broad range of graph-based research applications,
                   including but not limited to testing, benchmarking and performance-analysis of graph processing frameworks.
                   Pyrgg target audiences are computer scientists who study graph algorithms and graph processing frameworks.''',
  author = 'Sepand Haghighi',
  author_email = 'sepand@qpage.ir',
  url = 'https://github.com/sepandhaghighi/pyrgg',
  download_url = 'https://github.com/sepandhaghighi/pyrgg/tarball/v0.2',
  keywords = ['random', 'graph', 'python3','python','generator',"graph-process","generator",
              "moduland","DIMACS","JSON","YAML","Pickle","CSV","WEL","ASP","TGF","UCINET",
              ],
  install_requires=[
      'pyyaml',
	  'codecov',
      ],
  classifiers = [],
  license='MIT',
)
