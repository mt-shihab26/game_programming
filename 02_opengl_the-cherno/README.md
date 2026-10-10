# 02_opengl_the-cherno

## Requirements

Install these for your OS:

- [Clang](https://clang.llvm.org/), the compiler the project is built with
- [premake5](https://premake.github.io/), which generates the build files

## Building and running (Linux)

The scripts use bash and make, so they only work on Linux:

```bash
./scripts/generate.sh   # remove all generated and built files, then generate the makefiles (rerun after editing build.lua or adding source files)
./scripts/debug.sh      # build in debug configuration
./scripts/dev.sh        # build in debug configuration and run it
./scripts/release.sh    # regenerate, then build in release configuration (build/linux-x86_64/bin/release holds only the binary and its assets folder)
./scripts/clean.sh      # remove all generated and built files
```

Run `generate.sh` once before the first `debug.sh` or `dev.sh`; they only call
make and do not generate the makefiles themselves. `release.sh` does generate,
so it always builds from scratch and also wipes the debug build.
