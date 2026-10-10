#!/bin/bash

set -e

cd "$(dirname "$0")/.."

premake5 --file=build.lua clean-all
premake5 --file=build.lua gmake
