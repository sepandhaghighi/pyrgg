  set -e
  set -x
  python -m pytest pyrgg --cov=pyrgg --cov-report=term
  if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
      python -m vulture --min-confidence 80 --exclude=pyrgg,build,.eggs --sort-by-size .
  fi
  