#!/bin/bash

set -e

cd "$(dirname "$0")/.."

make config=debug -j"$(nproc)"

./build/linux-x86_64/bin/debug/demo
