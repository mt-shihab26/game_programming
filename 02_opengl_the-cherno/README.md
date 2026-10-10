# 02_opengl_the-cherno

## Requirements

Install these for your OS:

- [Clang](https://clang.llvm.org/), the compiler the project is built with
- [premake5](https://premake.github.io/), which generates the build files

## Building and running (Linux)

The scripts use bash and make, so they only work on Linux:

```bash
./scripts/generate.sh   # remove all generated and built files, then generate the makefiles
./scripts/debug.sh      # regenerate the demo makefile, then build in debug configuration
./scripts/dev.sh        # run debug.sh, then run the binary
./scripts/release.sh    # regenerate, then build in release configuration (build/linux-x86_64/bin/release holds only the binary and its assets folder)
./scripts/clean.sh      # remove all generated and built files, including GLFW and GLEW
```

For day-to-day work `./scripts/dev.sh` is enough, also on a fresh checkout.
`debug.sh` and `dev.sh` regenerate the demo makefile on every run, so new source
files are picked up without running `generate.sh`. They do not remove any
objects or binaries, so only changed files are recompiled.

`generate.sh` and `release.sh` remove everything first, so GLFW and GLEW are
rebuilt from scratch after them.
