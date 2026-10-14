#!/usr/bin/env bash

set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")/../.."

scripts/linux/debug.sh

exec build/linux-x86_64/bin/debug/demo "$@"
