
							


<div align="center">
<img src="http://www.shaghighi.ir/pyrgg/images/pyrgg-logo.png" height=240px width=320px>
<hr/>
<h1>Random Graph Generator</h1>

<a href="http://www.shaghighi.ir/pyrgg"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website"></a>
<a href="https://badge.fury.io/py/pyrgg"><img src="https://badge.fury.io/py/pyrgg.svg" alt="PyPI version" height="18"></a>
<a href="https://anaconda.org/sepandhaghighi/pyrgg"><img src="https://anaconda.org/sepandhaghighi/pyrgg/badges/version.svg"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pyrgg">
  <img src="https://codecov.io/gh/sepandhaghighi/pyrgg/branch/master/graph/badge.svg" alt="Codecov" /></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>

</div>	

----------
## Table of contents					
   * [Overview](https://github.com/sepandhaghighi/pyrgg#overview)
   * [Installation](https://github.com/sepandhaghighi/pyrgg#installation)
   * [Usage](https://github.com/sepandhaghighi/pyrgg#usage)
   * [Issues & Bug Reports](https://github.com/sepandhaghighi/pyrgg#issues--bug-reports)
   * [Todo](https://github.com/sepandhaghighi/pyrgg#todo)
   * [Sample Files](https://github.com/sepandhaghighi/pyrgg#sample-files)
   * [Example Of Usage](https://github.com/sepandhaghighi/pyrgg#example-of-usage)
   * [Supported Formats](https://github.com/sepandhaghighi/pyrgg#supported-formats)
   * [Similar Works](https://github.com/sepandhaghighi/pyrgg#similar-works)
   * [Dependencies](https://github.com/sepandhaghighi/pyrgg#dependencies)
   * [Contribution](https://github.com/sepandhaghighi/pyrgg/blob/master/.github/CONTRIBUTING.md)
   * [References](https://github.com/sepandhaghighi/pyrgg#references)
   * [Citing](https://github.com/sepandhaghighi/pyrgg#citing)
   * [Authors](https://github.com/sepandhaghighi/pyrgg/blob/master/AUTHORS.md)
   * [License](https://github.com/sepandhaghighi/pyrgg#license)
   * [Donate](https://github.com/sepandhaghighi/pyrgg#donate-to-our-project)
   * [Changelog](https://github.com/sepandhaghighi/pyrgg/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/sepandhaghighi/pyrgg/blob/master/.github/CODE_OF_CONDUCT.md)			
				
## Overview			
Pyrgg is an easy-to-use synthetic random graph generator written in Python which supports various graph file formats including <a href ="http://www.diag.uniroma1.it/challenge9/format.shtml">DIMACS .gr </a> files.
Pyrgg has the ability to generate graphs of different sizes and is designed to provide input files for broad range of graph-based research applications, including but not limited to testing, benchmarking and performance-analysis of graph processing frameworks.
Pyrgg target audiences are computer scientists who study graph algorithms and graph processing frameworks.

<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/pyrgg"><img src="https://www.openhub.net/p/pyrgg/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/count/pyrgg"><img src="http://pepy.tech/badge/pyrgg"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/pyrgg"><img src="https://img.shields.io/github/stars/sepandhaghighi/pyrgg.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/pyrgg"><img src="https://travis-ci.org/sepandhaghighi/pyrgg.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/sepandhaghighi/pyrgg"><img src="https://travis-ci.org/sepandhaghighi/pyrgg.svg?branch=dev"></a></a></td>
	</tr>
	<tr>
		<td align="center">AppVeyor</td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/pyrgg"><img src="https://ci.appveyor.com/api/projects/status/j9g3xikmh1elti13/branch/master?svg=true"></a></td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/pyrgg"><img src="https://ci.appveyor.com/api/projects/status/j9g3xikmh1elti13/branch/dev?svg=true"></a></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codacy.com/app/sepand-haghighi/pyrgg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pyrgg&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/11ec048bcd594d84997380b64d2d4add"/></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/pyrgg"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/pyrgg/badge" alt="CodeFactor" /></a></td>		
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 0.8](https://github.com/sepandhaghighi/pyrgg/archive/v0.8.zip) or [Latest Source ](https://github.com/sepandhaghighi/pyrgg/archive/dev.zip)
- `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install pyrgg==0.8` or `pip3 install pyrgg==0.8` (Need root access)							

### Conda

- Check [Conda Managing Package](https://conda.io)
- `conda install -c sepandhaghighi pyrgg` (Need root access)	

### Exe Version (Only Windows)
- Download [Exe-Version 0.8](https://github.com/sepandhaghighi/pyrgg/releases/download/v0.8/PYRGG-0.8.exe)
- Run `PYRGG-0.8.exe`

### System Requirements
Pyrgg will likely run on a modern dual core PC. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 4GB of RAM

Note that it may run on lower end equipment though good performance is not guaranteed.		


## Usage			

<div align="center">

<a href="https://asciinema.org/a/352310" target="_blank"><img src="https://asciinema.org/a/352310.svg" /></a>

</div>


## Issues & Bug Reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [info@pyrgg.ir](mailto:info@pyrgg.ir "info@pyrgg.ir"). 

## TODO	
- [x] Formats
  - [x] DIMACS
  - [x] JSON
  - [x] YAML
  - [x] Pickle 
  - [x] CSV
  - [x] TSV
  - [x] WEL	
  - [x] ASP
  - [x] TGF
  - [x] UCINET DL
  - [x] GML
  - [x] GDF
  - [x] Matrix Market
  - [x] Graph Line
  - [ ] GEXF
- [ ] Sizes
  - [x] Small
  - [x] Medium
  - [ ] Large
- [x] Weighted Graph															
	- [x] Signed Weights
- [x] Unweighted Graph
- [x] Dense Graph
- [x] Sparse Graph
- [x] Directed Graph
- [x] Self loop
- [x] Parallel Arc
- [ ] Multithreading
- [ ] GUI
- [ ] Erdős–Rényi model
- [ ] Tree

## Sample Files
- [Sample 1-DIMACS](https://www.dropbox.com/s/i80tnwuuv4iyqet/100.gr.gz?dl=0) (100 Vertices , 3KB)
- [Sample 2-DIMACS](https://www.dropbox.com/s/lqk42pwu7o4xauv/1000.gr.gz?dl=0) (1000 Vertices , 13KB)
- [Sample 3-DIMACS](https://www.dropbox.com/s/93dp8cjs6lnu83u/1000000.gr.gz?dl=0) (1000000 Vertices , 7MB)
- [Sample 4-DIMACS](https://www.dropbox.com/s/rrxdc4wt0ldonfk/5000000.gr.gz?dl=0) (5000000 Vertices , 37MB)
- [Sample 1-JSON](https://www.dropbox.com/s/yvevoyb8559nytb/100.json?dl=0) (100 Vertices , 11KB)
- [Sample 2-JSON](https://www.dropbox.com/s/f6kljlch7p2rfhy/1000.json?dl=0) (1000 Vertices , 105KB)
- [Sample 1-CSV](https://www.dropbox.com/s/dmld0eadftnatr5/100.csv?dl=0) (100 Vertices , 3KB)
- [Sample 2-CSV](https://www.dropbox.com/s/juxah4nwamzdegr/1000.csv?dl=0) (1000 Vertices , 51KB)
- [Sample 1-TSV](https://www.dropbox.com/s/j3zgs4kx2paxe75/100.tsv?dl=0) (100 Vertices , 29KB)
- [Sample 2-TSV](https://www.dropbox.com/s/ykagmjgwlpim6dq/1000.tsv?dl=0) (1000 Vertices , 420KB)
- [Sample 1-WEL](https://www.dropbox.com/s/moie1xb2wj90y33/100.wel?dl=0) (100 Vertices , 5KB)
- [Sample 2-WEL](https://www.dropbox.com/s/h6pohl60okhdnt7/1000.wel?dl=0) (1000 Vertices , 192KB)
- [Sample 1-YAML](https://www.dropbox.com/s/9seljohtoqjzjzy/30.yaml?dl=0) (30 Vertices , 3KB)
- [Sample 2-YAML](https://www.dropbox.com/s/wtfh38rgmn29npi/100.yaml?dl=0) (100 Vertices , 12KB)
- [Sample 1-LP](https://www.dropbox.com/s/4bufa1m4uamv48z/100.lp?dl=0) (100 Vertices , 7KB)
- [Sample 2-LP](https://www.dropbox.com/s/w79fh1qva64namw/1000.lp?dl=0) (1000 Vertices , 76KB)
- [Sample 1-Pickle](https://www.dropbox.com/s/4s8zt9i13z39gts/100.p?dl=0) (100 Vertices , 15KB)
- [Sample 2-Pickle](https://www.dropbox.com/s/fzurqu5au0p1b54/1000.p?dl=0) (1000 Vertices , 209KB)
- [Sample 1-TGF](https://www.dropbox.com/s/tehb6f3gz2o5v9c/100.tgf?dl=0) (100 Vertices , 4KB)
- [Sample 2-TGF](https://www.dropbox.com/s/9mjeq4w973189cc/1000.tgf?dl=0) (1000 Vertices , 61KB)
- [Sample 1-UCINET DL](https://www.dropbox.com/s/82wrl86uowwjud2/100.dl?dl=0) (100 Vertices , 8KB)
- [Sample 2-UCINET DL](https://www.dropbox.com/s/kbzbsy47uvfqdsi/1000.dl?dl=0) (1000 Vertices , 729KB)
- [Sample 1-MTX](https://www.dropbox.com/s/ztw3vg0roups82q/100.mtx?dl=0) (100 Vertices , 59KB)
- [Sample 2-MTX](https://www.dropbox.com/s/skjjvbbzrpvryl4/1000.mtx?dl=0) (1000 Vertices , 1.8MB)
- [Sample 1-GL](https://www.dropbox.com/s/obmmb5nw1lca9z3/100.gl?dl=0) (100 Vertices , 17KB)
- [Sample 2-GL](https://www.dropbox.com/s/intufsbudnmfv8m/1000.gl?dl=0) (1000 Vertices , 2.4MB)
- [Sample 1-GDF](https://www.dropbox.com/s/7dqox0f8e1f859s/100.gdf?dl=0) (100 Vertices , 21KB)
- [Sample 2-GDF](https://www.dropbox.com/s/xabjzpp0p5sr4b9/1000.gdf?dl=0) (1000 Vertices , 690KB)
- [Sample 1-GML](https://www.dropbox.com/s/g9uvywn1fwt9aq7/100.gml?dl=0) (100 Vertices , 120KB)
- [Sample 2-GML](https://www.dropbox.com/s/5gt5udezy56mlz9/1000.gml?dl=0) (1000 Vertices , 2.4MB)




## Example Of Usage


- Generate synthetic data for graph processing frameworks (some of them mentioned here) performance-analysis 			 
	- [Medusa](https://github.com/JianlongZhong/Medusa "Medusa") 
	- [Totem](https://github.com/netsyslab/Totem "Totem")
	- [Frog](https://github.com/AndrewStallman/Frog "Frog")
	- [CuSha](https://github.com/farkhor/CuSha "CuSha")
<div align="center">
<img src="https://www.pyrgg.ir/images/random.png">
<p>Fig. 1. Rand Graph Generation</p>
</div>

- Generate synthetic data for graph benchmark suite like [GAP](https://github.com/sbeamer/gapbs) 


## Supported Formats 			

- [DIMACS(.gr)](http://www.diag.uniroma1.it/challenge9/format.shtml)
	```
		p sp <number of vertices> <number of edges>
		a <head_1> <tail_1> <weight_1>

		.
		.
		.
		
		a <head_n> <tail_n> <weight_n>
	```
- [CSV(.csv)](https://en.wikipedia.org/wiki/Comma-separated_values)
	```
		<head_1>,<tail_1>,<weight_1>

		.
		.
		.
		
		<head_n>,<tail_n>,<weight_n>
	```

- [TSV(.tsv)](https://en.wikipedia.org/wiki/Tab-separated_values)
	```
		<head_1>	<tail_1>	<weight_1>

		.
		.
		.
		
		<head_n>	<tail_n>	<weight_n>
	```

- [JSON(.json)](https://en.wikipedia.org/wiki/JSON)

	```
		{
		"graph": {
				"nodes":[
				{
					"id": "1"
				},

				.
				.
				.
				{
					"id": "n"
				}
				],
				"edges":[
				{
					"source": "head_1",
					"target": "tail_1",
					"weight": "weight_1"
				},

				.
				.
				.

				{
					"source": "head_n",
					"target": "tail_n",
					"weight": "weight_n"
				},
				]
			}
		}
	```
- [YAML(.yaml)](https://en.wikipedia.org/wiki/YAML)
	```
		graph:
  			edges:
			- source: "head_1"
    	  	target: "tail_1"
    	  	weight: "weight_1"
		
			.
			.
			.

			- source: "head_n"
    	  	target: "tail_n"
    	  	weight: "weight_n"
						
			nodes:
  			- id: '1'
  
  			.
			.
			.

			- id: 'n'

	```
- [Weighted Edge List(.wel)](http://www.cs.cmu.edu/~pbbs/benchmarks/graphIO.html)	
	```
		<head_1> <tail_1> <weight_1>
		
		.
		.
		.
		
		<head_n> <tail_n> <weight_n>	
	```
- [ASP(.lp)](https://www.mat.unical.it/aspcomp2013/MaximalClique)
	```
		node(1).
		.
		.
		.
		node(n).
		edge(head_1,tail_1,weight_1).
		.
		.
		.
		edge(head_n,tail_n,weight_n).
	```
- [Trivial_Graph_Format(.tgf)](https://en.wikipedia.org/wiki/Trivial_Graph_Format)
	```
		1
		.
		.
		.
		n
		#
		1 2 weight_1
		.
		.
		.
		n k weight_n
	```
- [UCINET DL Format(.dl)](https://sites.google.com/site/ucinetsoftware/home)
	```
		dl
		format=edgelist1
		n=<number of vertices>
		data:
		1 2 weight_1
		.
		.
		.
		n k weight_n	
	```
- [Matrix Market(.mtx)](https://math.nist.gov/MatrixMarket/formats.html)
   ```
	   %%MatrixMarket matrix coordinate real general
       <number of vertices>  <number of vertices>  <number of edges>
       <head_1>    <tail_1>    <weight_1> 
       .
       .
       .
       <head_n>    <tail_n>    <weight_n> 
   ```
- Graph Line(.gl)
	```
	   <head_1> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
	   <head_2> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
	   .
	   .
	   .
	   <head_n> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
	```

- GDF(.gdf)
	```
	   nodedef>name VARCHAR,label VARCHAR
       node_1,node_1_label
       node_2,node_2_label
       .
       .
       .
       node_n,node_n_label
       edgedef>node1 VARCHAR,node2 VARCHAR, weight DOUBLE
       node_1,node_2,weight_1
       node_1,node_3,weight_2
       .
       .
       .
       node_n,node_2,weight_n 
	```

- [GML(.gml)](https://en.wikipedia.org/wiki/Graph_Modelling_Language)
	```
       graph
	   [
         multigraph 0
         directed  0
         node
         [
          id 1
          label "Node 1"
         ]
         node
         [
          id 2
          label "Node 2"
         ]
         .
         .
         .
         node
         [
          id n
          label "Node n"
         ]
         edge
         [
          source 1
          target 2
          value W1
         ]
         edge
         [
          source 2
          target 4
          value W2
         ]
         .
         .
         .
         edge
         [
          source n
          target r
          value Wn
         ]
       ]
	```

- [Pickle(.p)](https://docs.python.org/3.5/library/pickle.html) (Binary Format)	
 			

## Similar Works
- [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random graphs with tunable strength of community structure
- [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
- [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)


## Dependencies

<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/pyrgg/requirements/?branch=master"><img src="https://requires.io/github/sepandhaghighi/pyrgg/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/sepandhaghighi/pyrgg/requirements/?branch=dev"><img src="https://requires.io/github/sepandhaghighi/pyrgg/requirements.svg?branch=dev" alt="Requirements Status" /></a></td>
	</tr>
</table>


## Citing

If you use pyrgg in your research, please cite the [JOSS paper](http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26 "Pyrgg JOSS Paper") ;-)

<pre>
@article{Haghighi2017,
  doi = {10.21105/joss.00331},
  url = {https://doi.org/10.21105/joss.00331},
  year  = {2017},
  month = {sep},
  publisher = {The Open Journal},
  volume = {2},
  number = {17},
  author = {Sepand Haghighi},
  title = {Pyrgg: Python Random Graph Generator},
  journal = {The Journal of Open Source Software}
}
</pre>

<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a href="http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26"><img src="http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26/status.svg"></a></td>	
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://zenodo.org/badge/latestdoi/89410101"><img src="https://zenodo.org/badge/89410101.svg" alt="DOI"></a></td>
	</tr>
</table>
 			

## License

<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpyrgg?ref=badge_large" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsepandhaghighi%2Fpyrgg.svg?type=large"/></a>


## References
					

<div align="center">

<img src="http://www.shaghighi.ir/pyrgg/images/dimacs_logo.gif" alt="DIMACS">


</div>  						
 
## Donate to our project		
							

<h3>Bitcoin :</h3>					

```1XGr9qbZjBpUQJJSB6WtgBQbDTgrhPLPA```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	