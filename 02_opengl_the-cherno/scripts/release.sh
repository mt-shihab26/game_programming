#!/bin/bash

set -e

cd "$(dirname "$0")/.."

./scripts/generate.sh

make config=release -j"$(nproc)"
