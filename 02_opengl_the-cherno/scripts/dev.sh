#!/bin/bash

set -e
cd "$(dirname "$0")/.."

make config=debug -j"$(nproc)"

./bin/debug/demo
