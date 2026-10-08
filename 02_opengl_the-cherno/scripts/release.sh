#!/bin/bash

set -e

cd "$(dirname "$0")/.."

premake5 --file=build.lua clean

premake5 --file=build.lua gmake

make config=release -j"$(nproc)"
