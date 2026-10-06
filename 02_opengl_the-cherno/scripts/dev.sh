#!/bin/bash

set -e
cd "$(dirname "$0")/.."

config="${1:-debug}"

make config="$config" -j"$(nproc)"

"./bin/$config/demo"
