---
title: 'pyrgg: Python Random Graph Generator'
tags:
  - graph
  - script
  - generator
  - processing
  - random
authors:
 - name: Sepand Haghighi
   orcid: 0000-0001-9450-2375
   affiliation: 1
affiliations:
 - name: Moduland Co
   index: 1
date: 18 July 2017
---
						

# Summary
Pyrgg is an easy to use synthetic random graph generator based on DIMACS/JSON format written in python
Pyrgg has the ability to generate graphs in different sizes and designed to provide input files for 
test, benchmark and performance analysis of graph processing frameworks, but it can be used in any other research program that include graphs in DIMACS/JSON format.

Pyrgg can generate graphs with this specs :

- Weighted
- Signed
- Self Loop
- Parallel Arc
- Sparse
- Dense  

This application get :
					
- vertices number
- max weight
- min weight
- max edge number(for each vertex)
- min edge number(for each vertex)

and generate graph in flat file format (*.gr) and JSON.

![outputformat](outputformat.jpg)

# References
