#!/bin/bash

set -e
cd "$(dirname "$0")"

config="${1:-debug}"

premake5 gmake
make config="$config" -j"$(nproc)"

"./bin/$config/demo"
