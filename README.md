
							


<div align="center">
<img src="http://www.shaghighi.ir/pyrgg/images/pyrgg-logo.png" height=240px width=320px>
<hr/>
<h1>Random Graph Generator</h1>
<a href="https://scrutinizer-ci.com/g/sepandhaghighi/pyrgg/?branch=master"><img src="https://scrutinizer-ci.com/g/sepandhaghighi/pyrgg/badges/quality-score.png?b=master"></a>
<a href="https://www.codacy.com/app/sepand-haghighi/pyrgg?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sepandhaghighi/pyrgg&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/11ec048bcd594d84997380b64d2d4add"/></a>
<a href="https://travis-ci.org/sepandhaghighi/pyrgg"><img src="https://travis-ci.org/sepandhaghighi/pyrgg.svg?branch=master"></a>
<a href="http://www.shaghighi.ir/pyrgg"><img src="https://img.shields.io/website-up-down-green-red/http/shields.io.svg?label=website"></a>
<a href="https://badge.fury.io/py/pyrgg"><img src="https://badge.fury.io/py/pyrgg.svg" alt="PyPI version" height="18"></a>
<a href="https://zenodo.org/badge/latestdoi/89410101"><img src="https://zenodo.org/badge/89410101.svg" alt="DOI"></a>
<a href="http://sepandhaghighi.github.io/pyrgg/doc"><img src="https://img.shields.io/badge/doc-latest-red.svg"></a>
</div>				
				
## Overview
pyrgg is a synthetic random graph generator based on <a href ="http://www.diag.uniroma1.it/challenge9/format.shtml">DIMACS</a> format
this software generate input file for graph processing applications.  



## Installation		

### Source Code
- Download [Version 0.1](https://github.com/sepandhaghighi/pyrgg/archive/v0.1.zip) or [Latest Source ](https://github.com/sepandhaghighi/pyrgg/archive/master.zip)

- `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install pyrgg` or `pip3 install pyrgg` (Need root access)							
			



## Usage ##
[Download Full Run Video](http://www.shaghighi.ir/pyrgg/videos/FullRun.mkv "Video") (2.8 MB - MKV)( This video recorded by [simplescreenrecorder](http://www.maartenbaert.be/simplescreenrecorder/ "simplescreenrecorder") )				

<div align="center">

<img src="http://www.shaghighi.ir/pyrgg/images/pyrgg.gif" alt="pyrgg usage" title="pyrgg usage">
<br/>
<img src="http://www.shaghighi.ir/pyrgg/images/output.jpg" alt="pyrgg output" title="pyrgg output" width=800px>

</div>


## Test			



`python3 -m pyrgg test` or `python -m pyrgg test`
			
This test run automatically in each commit ;-) 						

Linux : <a href="https://travis-ci.org/sepandhaghighi/pyrgg"><img src="https://travis-ci.org/sepandhaghighi/pyrgg.svg?branch=master"></a>							

Windows : <a href="https://ci.appveyor.com/project/sepandhaghighi/pyrgg"><img src="https://ci.appveyor.com/api/projects/status/j9g3xikmh1elti13?svg=true"></a>						
			
<div align="center">

<img src="http://www.shaghighi.ir/pyrgg/images/test.gif" alt="pyrgg test" title="pyrgg test">


</div>


## Issues & Bug Reports			

Just fill an issue and describe it. I'll check it ASAP!							
or send an email to [sepand@qpage.ir](mailto:sepand@qpage.ir "sepand@qpage.ir"). 

## TODO		
- [ ] Sizes
  - [x] Small
  - [x] Medium
  - [ ] Large
- [x] Weighted Graph															
	- [x] Signed Weights
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
- [Sample 1](https://www.dropbox.com/s/i80tnwuuv4iyqet/100.gr.gz?dl=0) (100 Vertices , 3KB)
- [Sample 2](https://www.dropbox.com/s/lqk42pwu7o4xauv/1000.gr.gz?dl=0) (1000 Vertices , 13KB)
- [Sample 3](https://www.dropbox.com/s/93dp8cjs6lnu83u/1000000.gr.gz?dl=0) (1000000 Vertices , 7MB)
- [Sample 4](https://www.dropbox.com/s/rrxdc4wt0ldonfk/5000000.gr.gz?dl=0) (5000000 Vertices , 37MB)


## Application			
This software can be used for generation of input files in parallel sparse graph applications benchmark like :			


- [Medusa](https://github.com/JianlongZhong/Medusa "Medusa") 
- [Totem](https://github.com/netsyslab/Totem "Totem")
- [Frog](https://github.com/AndrewStallman/Frog "Frog")
- [CuSha](https://github.com/farkhor/CuSha "CuSha")




## Contribution			

You can fork the repository, improve or fix some part of it and then send the pull requests back if you want to see them here. I really appreciate that. ❤️			

Remember to write a few tests for your code before sending pull requests. 			

## Similar Works
- [Random Modular Network Generator](https://github.com/prathasah/random-modular-network-generator) Generates random graphs with tunable strength of community structure
- [randomGraph](https://github.com/sdghafouri/randomGraph) very simple random graph generator in matlab
- [Graph1](https://github.com/Saptaparni/Graph1) Random Graph Generator with Max capacity paths (C++)


## Citing

If you use pyrgg in your research , please cite this ;-)

<blockquote>
<p>[1]Sepand Haghighi. pyrgg : Python Random Graph Generator 2017. doi:10.5281/zenodo.830031</p>
</blockquote>
 			

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