#!/bin/bash

set -e
cd "$(dirname "$0")/.."

premake5 clean
premake5 gmake
make config=release -j"$(nproc)"
