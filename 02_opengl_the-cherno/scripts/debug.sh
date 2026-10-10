#!/bin/bash

set -e

cd "$(dirname "$0")/.."

premake5 --file=build.lua clean-demo
premake5 --file=build.lua gmake

make config=debug -j"$(nproc)"
