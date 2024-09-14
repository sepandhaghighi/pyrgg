<div align="center">
	<img src="https://github.com/sepandhaghighi/pyrgg/raw/master/otherfile/logo.png" width="450">
	<h1>PyRGG: Python Random Graph Generator</h1>
	<a href="https://www.pyrgg.site"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website"></a>
	<a href="https://badge.fury.io/py/pyrgg"><img src="https://badge.fury.io/py/pyrgg.svg" alt="PyPI version" height="18"></a>
	<a href="https://anaconda.org/sepandhaghighi/pyrgg"><img src="https://anaconda.org/sepandhaghighi/pyrgg/badges/version.svg"></a>
	<a href="https://codecov.io/gh/sepandhaghighi/pyrgg"><img src="https://codecov.io/gh/sepandhaghighi/pyrgg/branch/master/graph/badge.svg" alt="Codecov"></a>
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
	<a href="https://discord.gg/dfYAWVMaCW"><img src="https://img.shields.io/discord/1013411447130308669.svg" alt="Discord Channel"></a>
</div>			
				
## Overview	

<p align="justify">		
PyRGG is a user-friendly synthetic random graph generator that is written in Python and supports multiple graph file formats, such as <a href ="https://www.diag.uniroma1.it/challenge9/format.shtml#graph">DIMACS-Graph</a> files. It can generate graphs of various sizes and is specifically designed to create input files for a wide range of graph-based research applications, including testing, benchmarking, and performance analysis of graph processing frameworks. PyRGG is aimed at computer scientists who are studying graph algorithms and graph processing frameworks.
</p>

<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/pyrgg"><img src="https://www.openhub.net/p/pyrgg/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/pyrgg"><img src="http://pepy.tech/badge/pyrgg"></a></td>
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
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pyrgg/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/pyrgg/workflows/CI/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codacy.com/app/sepand-haghighi/pyrgg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pyrgg&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/11ec048bcd594d84997380b64d2d4add"/></a></td>	
        <td align="center"><a href="https://codebeat.co/projects/github-com-sepandhaghighi-pyrgg-dev"><img alt="codebeat badge" src="https://codebeat.co/badges/3f6c7449-3dfc-406b-b233-9fe615c2d103" /></a></td>	
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/pyrgg"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/pyrgg/badge" alt="CodeFactor" /></a></td>	
	</tr>
</table>


## Installation		

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install pyrgg==1.5`						

### Source Code
- Download [Version 1.5](https://github.com/sepandhaghighi/pyrgg/archive/v1.5.zip) or [Latest Source ](https://github.com/sepandhaghighi/pyrgg/archive/dev.zip)
- `pip install .`

### Conda
- Check [Conda Managing Package](https://conda.io)
- `conda install -c sepandhaghighi pyrgg`

### Exe Version (Only Windows)
- Download [Exe-Version 1.5](https://github.com/sepandhaghighi/pyrgg/releases/download/v1.5/PYRGG-1.5.exe)
- Run `PYRGG-1.5.exe`

### System Requirements
Pyrgg will likely run on a modern dual core PC. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 4GB of RAM

Note that it may run on lower end equipment though good performance is not guaranteed.		


## Usage
- Open `CMD` (Windows) or `Terminal` (Linux)
- Run `pyrgg` or `python -m pyrgg` (or run `PYRGG.exe`)
- Enter data		

<div align="center">

<a href="https://asciinema.org/a/539844" target="_blank"><img src="https://asciinema.org/a/539844.svg" /></a>

</div>

## Engines

### PyRGG

<table>
	<tr>
		<th>Parameter</th>
		<th>Description</th>
	</tr>
	<tr>
		<td align="center">Vertices Number</td>
		<td align="center">The total number of vertices in the graph</td>
	</tr>
	<tr>
		<td align="center">Min Edge Number</td>
		<td align="center">The minimum number of edges connected to each vertex</td>
	</tr>
	<tr>
		<td align="center">Max Edge Number</td>
		<td align="center">The maximum number of edges connected to each vertex</td>
	</tr>
	<tr>
		<td align="center">Weighted / Unweighted</td>
		<td align="center">Specifies whether the graph is weighted or unweighted</td>
	</tr>
	<tr>
		<td align="center">Min Weight</td>
		<td align="center">The minimum weight of the edges (if weighted)</td>
	</tr>
	<tr>
		<td align="center">Max Weight</td>
		<td align="center">The maximum weight of the edges (if weighted)</td>
	</tr>
	<tr>
		<td align="center">Signed / Unsigned</td>
		<td align="center">Specifies whether the edge weights are signed or unsigned</td>
	</tr>
	<tr>
		<td align="center">Directed / Undirected</td>
		<td align="center">Specifies whether the graph is directed or undirected</td>
	</tr>
	<tr>
		<td align="center">Self Loop / No Self Loop</td>
		<td align="center">Specifies whether self-loop is allowed or not</td>
	</tr>
	<tr>
		<td align="center">Simple / Multigraph</td>
		<td align="center">Specifies whether the graph is a simple graph or a multigraph</td>
	</tr>
</table>

### Erdős–Rényi-Gilbert

<table>
	<tr>
		<th>Parameter</th>
		<th>Description</th>
	</tr>
	<tr>
		<td align="center">Vertices Number</td>
		<td align="center">The total number of vertices in the graph</td>
	</tr>
	<tr>
		<td align="center">Probability</td>
		<td align="center">The probability for edge creation between any two vertices</td>
	</tr>
	<tr>
		<td align="center">Directed / Undirected</td>
		<td align="center">Specifies whether the graph is directed or undirected</td>
	</tr>
</table>


## Supported Formats 			

### DIMACS

```
	p sp <number of vertices> <number of edges>
	a <head_1> <tail_1> <weight_1>

	.
	.
	.
		
	a <head_n> <tail_n> <weight_n>
```

* [Document](http://www.diag.uniroma1.it/challenge9/format.shtml)
* [Sample 1](https://www.dropbox.com/s/i80tnwuuv4iyqet/100.gr.gz?dl=0) (100 Vertices , 3KB)
* [Sample 2](https://www.dropbox.com/s/lqk42pwu7o4xauv/1000.gr.gz?dl=0) (1000 Vertices , 13KB)
* [Sample 3](https://www.dropbox.com/s/93dp8cjs6lnu83u/1000000.gr.gz?dl=0) (1000000 Vertices , 7MB)
* [Sample 4](https://www.dropbox.com/s/rrxdc4wt0ldonfk/5000000.gr.gz?dl=0) (5000000 Vertices , 37MB)

### CSV

```
	<head_1>,<tail_1>,<weight_1>

	.
	.
	.
		
	<head_n>,<tail_n>,<weight_n>
```

* [Document](https://en.wikipedia.org/wiki/Comma-separated_values)
* [Sample 1](https://www.dropbox.com/s/dmld0eadftnatr5/100.csv?dl=0) (100 Vertices , 3KB)
* [Sample 2](https://www.dropbox.com/s/juxah4nwamzdegr/1000.csv?dl=0) (1000 Vertices , 51KB)

### TSV

```
	<head_1>	<tail_1>	<weight_1>

	.
	.
	.
		
	<head_n>	<tail_n>	<weight_n>
```

* [Document](https://en.wikipedia.org/wiki/Tab-separated_values)
* [Sample 1](https://www.dropbox.com/s/j3zgs4kx2paxe75/100.tsv?dl=0) (100 Vertices , 29KB)
* [Sample 2](https://www.dropbox.com/s/ykagmjgwlpim6dq/1000.tsv?dl=0) (1000 Vertices , 420KB)

### JSON

```
{
	"properties": {
		"directed": true,
		"signed": true,
		"multigraph": true,
		"weighted": true,
		"self_loop": true
	},
	"graph": {
		"nodes":[
		{
			"id": 1
		},

		.
		.
		.

		{
			"id": n
		}
		],
		"edges":[
		{
			"source": head_1,
			"target": tail_1,
			"weight": weight_1
		},

		.
		.
		.

		{
			"source": head_n,
			"target": tail_n,
			"weight": weight_n
		}
		]
	}
}
```

* [Document](https://en.wikipedia.org/wiki/JSON)
* [Sample 1](https://www.dropbox.com/s/yvevoyb8559nytb/100.json?dl=0) (100 Vertices , 26KB)
* [Sample 2](https://www.dropbox.com/s/f6kljlch7p2rfhy/1000.json?dl=0) (1000 Vertices , 494KB)

### YAML
```
 	graph:
 		edges:
 		- source: head_1
 	  	target: tail_1
 	  	weight: weight_1
 	
 		.
 		.
 		.

 		- source: head_n
 	  	target: tail_n
 	  	weight: weight_n
 					
 		nodes:
 		- id: 1

 		.
 		.
 		.

 		- id: n
 	properties:
 		directed: true
 		multigraph: true
 		self_loop: true
 		signed: true
 		weighted: true
```

* [Document](https://en.wikipedia.org/wiki/YAML)
* [Sample 1](https://www.dropbox.com/s/9seljohtoqjzjzy/30.yaml?dl=0) (30 Vertices , 6KB)
* [Sample 2](https://www.dropbox.com/s/wtfh38rgmn29npi/100.yaml?dl=0) (100 Vertices , 35KB)

### Weighted Edge List	
```
	<head_1> <tail_1> <weight_1>
		
	.
	.
	.
		
	<head_n> <tail_n> <weight_n>	
```

* [Document](http://www.cs.cmu.edu/~pbbs/benchmarks/graphIO.html)
* [Sample 1](https://www.dropbox.com/s/moie1xb2wj90y33/100.wel?dl=0) (100 Vertices , 5KB)
* [Sample 2](https://www.dropbox.com/s/h6pohl60okhdnt7/1000.wel?dl=0) (1000 Vertices , 192KB)

### ASP

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

* [Document](https://www.mat.unical.it/aspcomp2013/MaximalClique)
* [Sample 1](https://www.dropbox.com/s/4bufa1m4uamv48z/100.lp?dl=0) (100 Vertices , 7KB)
* [Sample 2](https://www.dropbox.com/s/w79fh1qva64namw/1000.lp?dl=0) (1000 Vertices , 76KB)

### Trivial Graph Format

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
* [Document](https://en.wikipedia.org/wiki/Trivial_Graph_Format)
* [Sample 1](https://www.dropbox.com/s/tehb6f3gz2o5v9c/100.tgf?dl=0) (100 Vertices , 4KB)
* [Sample 2](https://www.dropbox.com/s/9mjeq4w973189cc/1000.tgf?dl=0) (1000 Vertices , 61KB)

### UCINET DL Format

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
* [Document](https://sites.google.com/site/ucinetsoftware/home)
* [Sample 1](https://www.dropbox.com/s/82wrl86uowwjud2/100.dl?dl=0) (100 Vertices , 8KB)
* [Sample 2](https://www.dropbox.com/s/kbzbsy47uvfqdsi/1000.dl?dl=0) (1000 Vertices , 729KB)

### Matrix Market

```
    %%MatrixMarket matrix coordinate real general
    <number of vertices>  <number of vertices>  <number of edges>
    <head_1>    <tail_1>    <weight_1> 
    .
    .
    .
    <head_n>    <tail_n>    <weight_n> 
```
* [Document](https://math.nist.gov/MatrixMarket/formats.html)
* [Sample 1](https://www.dropbox.com/s/ztw3vg0roups82q/100.mtx?dl=0) (100 Vertices , 59KB)
* [Sample 2](https://www.dropbox.com/s/skjjvbbzrpvryl4/1000.mtx?dl=0) (1000 Vertices , 1.8MB)

### Graph Line
```
	<head_1> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
	<head_2> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
	.
	.
	.
	<head_n> <tail_1>:<weight_1> <tail_2>:<weight_2>  ... <tail_n>:<weight_n>
```

* [Sample 1](https://www.dropbox.com/s/obmmb5nw1lca9z3/100.gl?dl=0) (100 Vertices , 17KB)
* [Sample 2](https://www.dropbox.com/s/intufsbudnmfv8m/1000.gl?dl=0) (1000 Vertices , 2.4MB)

### GDF

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

* [Sample 1](https://www.dropbox.com/s/7dqox0f8e1f859s/100.gdf?dl=0) (100 Vertices , 21KB)
* [Sample 2](https://www.dropbox.com/s/xabjzpp0p5sr4b9/1000.gdf?dl=0) (1000 Vertices , 690KB)

### GML

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

* [Document](https://en.wikipedia.org/wiki/Graph_Modelling_Language)
* [Sample 1](https://www.dropbox.com/s/g9uvywn1fwt9aq7/100.gml?dl=0) (100 Vertices , 120KB)
* [Sample 2](https://www.dropbox.com/s/5gt5udezy56mlz9/1000.gml?dl=0) (1000 Vertices , 2.4MB)

### GEXF

```
     <?xml version="1.0" encoding="UTF-8"?>
     <gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">
         <meta lastmodifieddate="2009-03-20">
             <creator>PyRGG</creator>
             <description>File Name</description>
         </meta>
         <graph defaultedgetype="directed">
             <nodes>
                 <node id="1" label="Node 1" />
                 <node id="2" label="Node 2" />
                 ...
             </nodes>
             <edges>
                 <edge id="1" source="1" target="2" weight="400" />
                 ...
             </edges>
         </graph>
     </gexf>
```

* [Document](https://github.com/gephi/gexf/wiki/Basic-Concepts#network-topology)
* [Sample 1](https://www.dropbox.com/s/kgx8xl9j0dpk4us/100.gexf?dl=0) (100 Vertices , 63KB)
* [Sample 2](https://www.dropbox.com/s/7a380kf35buvusr/1000.gexf?dl=0) (1000 Vertices , 6.4MB)

### Graphviz

```
	graph example 
		{
		node1 -- node2 [weight=W1];
		node3 -- node4 [weight=W2];
		node1 -- node3 [weight=W3];
		.
		.
		.
		}
```

* [Document](https://graphviz.org/doc/info/lang.html)
* [Sample 1](https://www.dropbox.com/s/ukev1hi4kguomri/100.gv?dl=0) (100 Vertices , 11KB)
* [Sample 2](https://www.dropbox.com/s/vpvvliz96mdea1p/1000.gv?dl=0) (1000 Vertices , 106KB)
* [Online Visualization](https://dreampuf.github.io/GraphvizOnline/)

### Pickle

⚠️ Binary format

* [Document](https://docs.python.org/3.10/library/pickle.html)
* [Sample 1](https://www.dropbox.com/s/4s8zt9i13z39gts/100.p?dl=0) (100 Vertices , 12KB)
* [Sample 2](https://www.dropbox.com/s/fzurqu5au0p1b54/1000.p?dl=0) (1000 Vertices , 340KB)


## Example of Usage

- Generate synthetic data for graph processing frameworks (some of them mentioned here) performance-analysis 			 
	- [Medusa](https://github.com/JianlongZhong/Medusa "Medusa") 
	- [Totem](https://github.com/netsyslab/Totem "Totem")
	- [Frog](https://github.com/AndrewStallman/Frog "Frog")
	- [CuSha](https://github.com/farkhor/CuSha "CuSha")
- Generate synthetic data for graph benchmark suite like [GAP](https://github.com/sbeamer/gapbs) 

## Similar Works
- [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random graphs with tunable strength of community structure
- [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in MATLAB
- [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [info@pyrgg.site](mailto:info@pyrgg.site "info@pyrgg.site"). 

You can also join our discord server			

<a href="https://discord.gg/dfYAWVMaCW">
  <img src="https://img.shields.io/discord/1013411447130308669.svg?style=for-the-badge" alt="Discord Channel">
</a>


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
 			

## References
					

<blockquote>1- <a href="http://www.diag.uniroma1.it/challenge9/format.shtml">9th DIMACS Implementation Challenge - Shortest Paths</a> </blockquote>

<blockquote>2- <a href="http://www.cs.cmu.edu/~pbbs/benchmarks/graphIO.html">Problem Based Benchmark Suite</a></blockquote>

<blockquote>3- <a href="https://www.mat.unical.it/aspcomp2013/MaximalClique">MaximalClique - ASP Competition 2013</a></blockquote>

<blockquote>4- Pitas, Ioannis, ed. Graph-based social media analysis. Vol. 39. CRC Press, 2016. </blockquote>	

<blockquote>5- Roughan, Matthew, and Jonathan Tuke. "The hitchhikers guide to sharing graph data." 2015 3rd International Conference on Future Internet of Things and Cloud. IEEE, 2015. </blockquote>	

<blockquote>6- Borgatti, Stephen P., Martin G. Everett, and Linton C. Freeman. "Ucinet for Windows: Software for social network analysis." Harvard, MA: analytic technologies 6 (2002). </blockquote>

<blockquote>7- <a href="https://math.nist.gov/MatrixMarket/formats.html">Matrix Market: File Formats</a> </blockquote>		

<blockquote>8- <a href="https://socnetv.org/docs/formats.html#GML">Social Network Visualizer</a> </blockquote>

<blockquote>9- Adar, Eytan. "GUESS: a language and interface for graph exploration." Proceedings of the SIGCHI conference on Human Factors in computing systems. 2006. </blockquote>

<blockquote>10- Skiena, Steven S. The algorithm design manual. Springer International Publishing, 2020. </blockquote>

<blockquote>11- Chakrabarti, Deepayan, Yiping Zhan, and Christos Faloutsos. "R-MAT: A recursive model for graph mining." Proceedings of the 2004 SIAM International Conference on Data Mining. Society for Industrial and Applied Mathematics, 2004. </blockquote>

<blockquote>12- Zhong, Jianlong, and Bingsheng He. "An overview of medusa: simplified graph processing on gpus." ACM SIGPLAN Notices 47.8 (2012): 283-284.</blockquote>

<blockquote>13- Ellson, John, et al. "Graphviz and dynagraph—static and dynamic graph drawing tools." Graph drawing software. Springer, Berlin, Heidelberg, 2004. 127-148.</blockquote>

<blockquote>14- Gilbert, Edgar N. "Random graphs." The Annals of Mathematical Statistics 30.4 (1959): 1141-1144.</blockquote>

<blockquote>15- Erdős, Paul, and Alfréd Rényi. "On the strength of connectedness of a random graph." Acta Mathematica Hungarica 12.1 (1961): 261-267.</blockquote>


* Logo designed by [Zahra Mobasher](https://www.instagram.com/littleblackoyster)	
					
 
## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .			

<a href="http://www.pyrgg.site/donate.html" target="_blank"><img src="https://github.com/sepandhaghighi/pyrgg/raw/master/otherfile/donate-button.png" height="90px" width="270px" alt="PyRGG Donation"></a>

