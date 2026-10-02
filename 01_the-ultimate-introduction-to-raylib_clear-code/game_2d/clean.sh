#!/bin/bash

# Remove Python caches (__pycache__, *.pyc/*.pyo, tool caches), skipping virtualenvs.
cd "$(dirname "$0")" || exit 1

find . \( -name .venv -o -name venv -o -name .git \) -prune -o \
    \( -type d \( -name __pycache__ -o -name .pytest_cache -o -name .mypy_cache -o -name .ruff_cache \) -prune -exec rm -rf {} + \) -o \
    \( -type f -name '*.py[co]' -exec rm -f {} + \)
