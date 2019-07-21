  set -e
  set -x
  python version_check.py
  python -m pytest test --cov=pyrgg --cov-report=term
  if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture pyrgg --min-confidence 80 --sort-by-size
	  python -m bandit -r pyrgg -s B311,B403,B322
	  python -m pydocstyle --match-dir=pyrgg
  fi
  