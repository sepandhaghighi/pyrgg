  set -e
  set -x
  python -m pytest pyrgg --cov=pyrgg --cov-report=term
  