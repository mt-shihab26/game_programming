#!/bin/bash

set -e

cd "$(dirname "$0")/.."

./scripts/clean.sh

premake5 --file=build.lua gmake
