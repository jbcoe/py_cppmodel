#!/usr/bin/env bash

set -x

python -m pytype .
python -m unittest discover .
