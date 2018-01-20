
							


<div align="center">
<img src="http://www.shaghighi.ir/pyrgg/images/pyrgg-logo.png" height=240px width=320px>
<hr/>
<h1>Random Graph Generator</h1>
<a href="https://www.codacy.com/app/sepand-haghighi/pyrgg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pyrgg&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/11ec048bcd594d84997380b64d2d4add"/></a>
<a href="http://www.shaghighi.ir/pyrgg"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website"></a>
<a href="https://badge.fury.io/py/pyrgg"><img src="https://badge.fury.io/py/pyrgg.svg" alt="PyPI version" height="18"></a>
<a href="https://zenodo.org/badge/latestdoi/89410101"><img src="https://zenodo.org/badge/89410101.svg" alt="DOI"></a>
<a href="http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26"><img src="http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26/status.svg"></a>
<a href="http://sepandhaghighi.github.io/pyrgg/doc"><img src="https://img.shields.io/badge/doc-latest-red.svg"></a>
<a href="https://codecov.io/gh/sepandhaghighi/pyrgg">
  <img src="https://codecov.io/gh/sepandhaghighi/pyrgg/branch/master/graph/badge.svg" alt="Codecov" /></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>

</div>				
				
## Overview			
Pyrgg is an easy-to-use synthetic random graph generator written in Python which supports various graph file formats including <a href ="http://www.diag.uniroma1.it/challenge9/format.shtml">DIMACS .gr </a> files.
Pyrgg has the ability to generate graphs of different sizes and is designed to provide input files for broad range of graph-based research applications, including but not limited to testing, benchmarking and performance-analysis of graph processing frameworks.
Pyrgg target audiences are computer scientists who study graph algorithms and graph processing frameworks.


## Installation		

### Source Code
- Download [Version 0.2](https://github.com/sepandhaghighi/pyrgg/archive/v0.2.zip) or [Latest Source ](https://github.com/sepandhaghighi/pyrgg/archive/master.zip)
- `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install pyrgg` or `pip3 install pyrgg` (Need root access)							
			



## Usage			

<div align="center">

<a href="https://asciinema.org/a/141608" target="_blank"><img src="https://asciinema.org/a/141608.png" /></a>

<br/>
<img src="http://www.shaghighi.ir/pyrgg/images/output.jpg" alt="pyrgg output" title="pyrgg output" width=600px height=800px>
<p>Fig. 1. DIMACS .gr output format</p>

</div>


## Test			



`python3 -m pyrgg test` or `python -m pyrgg test`
			
This test run automatically in each commit ;-) 						
			
<div align="center">
<table style="border:1px solid black">
<tr>
<th>Linux</th>
<th>Windows</th>

</tr>

<tr>
<td><a href="https://travis-ci.org/sepandhaghighi/pyrgg"><img src="https://travis-ci.org/sepandhaghighi/pyrgg.svg?branch=master"></a></td>
<td> <a href="https://ci.appveyor.com/project/sepandhaghighi/pyrgg"><img src="https://ci.appveyor.com/api/projects/status/j9g3xikmh1elti13?svg=true"></a>	</td>

</tr>	

</table>

</div>	
													
<div align="center">

<img src="http://www.shaghighi.ir/pyrgg/images/test.gif" alt="pyrgg test" title="pyrgg test">


</div>


## Issues & Bug Reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 

## TODO	
- [x] Formats
  - [x] DIMACS
  - [x] JSON
  - [x] YAML
  - [x] Pickle 
  - [x] CSV
  - [x] WEL	
  - [x] ASP
  - [x] TGF
  - [x] UCINET DL
  - [ ] GEXF
- [ ] Sizes
  - [x] Small
  - [x] Medium
  - [ ] Large
- [x] Weighted Graph															
	- [x] Signed Weights
- [ ] Unweighted Graph
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




## Example Of Usage


- Generate synthetic data for graph processing frameworks (some of them mentioned here) performance-analysis 			 
	- [Medusa](https://github.com/JianlongZhong/Medusa "Medusa") 
	- [Totem](https://github.com/netsyslab/Totem "Totem")
	- [Frog](https://github.com/AndrewStallman/Frog "Frog")
	- [CuSha](https://github.com/farkhor/CuSha "CuSha")
<div align="center">
<img src="http://www.shaghighi.ir/pyrgg/images/random.png">
<p>Fig. 2. Rand Graph Generation</p>
</div>

- Generate synthetic data for graph benchmark suite like [GAP](https://github.com/sbeamer/gapbs) 


## Supported Formats 			

- [DIMACS(.gr)](http://www.diag.uniroma1.it/challenge9/format.shtml)
	```
		p sp <number of vertices> <number of directed edge>
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
- [Pickle(.p)](https://docs.python.org/3.5/library/pickle.html) (Binary Format)	



## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 			

## Similar Works
- [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random graphs with tunable strength of community structure
- [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
- [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)


## Citing

If you use pyrgg in your research , please cite the [JOSS paper](http://joss.theoj.org/papers/da33f691984d9a35f66ff93a391bbc26 "Pyrgg JOSS Paper") ;-)

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
 			

## License

<a href="https://github.com/sepandhaghighi/pyrgg/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mashape/apistatus.svg"/></a>


## Reference
					

<div align="center">

<img src="http://www.shaghighi.ir/pyrgg/images/dimacs_logo.gif" alt="DIMACS">


</div>  						
 
## Donate to our project
<h3>Beerpay :</h3>				

Hey dude! Help me out for a couple of :beers:!				


[![Beerpay](https://beerpay.io/sepandhaghighi/pyrgg/badge.svg?style=beer-square)](https://beerpay.io/sepandhaghighi/pyrgg)  [![Beerpay](https://beerpay.io/sepandhaghighi/pyrgg/make-wish.svg?style=flat-square)](https://beerpay.io/sepandhaghighi/pyrgg?focus=wish)									

<h3>Bitcoin :</h3>					

```1XGr9qbZjBpUQJJSB6WtgBQbDTgrhPLPA```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	