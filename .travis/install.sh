#!/bin/bash
# Dump Environment (so that we can check PATH, UT_FLAGS, etc.)
 set -e
 set -x
 PYTHON_COMMAND=python
 PIP_COMMAND=pip
 if [ "$TRAVIS_OS_NAME" == "osx" ]
 then
	 PYTHON_COMMAND=python3
	 PIP_COMMAND=pip3
 fi
 
 $PIP_COMMAND install -r requirements.txt
 $PYTHON_COMMAND setup.py install
 $PYTHON_COMMAND -m pyrgg test
 
 if [ "$TRAVIS_OS_NAME" == "osx" ]
 then
	$PIP_COMMAND install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt --user
  else
	$PIP_COMMAND install --upgrade --upgrade-strategy=only-if-needed -r dev-requirements.txt
 fi