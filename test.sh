#!/usr/bin/env bash

set -x

python3 -m pytype .
python3 -m unittest discover .
