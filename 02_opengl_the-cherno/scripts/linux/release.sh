#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/../.."

scripts/linux/generate.sh

make config=release -j"$(nproc)" "$@"
