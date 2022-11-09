#!/bin/bash

if ! python3 -m black tests/ ui/ --check; then
    echo 'black does not seem to have been run. Please run it before pushing'
    exit 1
fi
