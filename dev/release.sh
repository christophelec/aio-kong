#!/usr/bin/env sh

rm -rf dist
python setup.py sdist bdist_wheel
twine upload dist/*
