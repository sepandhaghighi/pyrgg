  set -e
  set -x
  python -m pytest test --cov=pyrgg --cov-report=term
  if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture pyrgg --min-confidence 80 --sort-by-size
	  python -m bandit -r pyrgg -s B311,B403
	  python -m pydocstyle --match-dir=pyrgg
  fi
  