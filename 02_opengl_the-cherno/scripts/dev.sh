#!/bin/bash

set -e

cd "$(dirname "$0")/.."

./scripts/debug.sh
./build/linux-x86_64/bin/debug/demo
