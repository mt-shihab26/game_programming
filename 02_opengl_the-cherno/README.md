# 02_opengl_the-cherno

## Requirements

Install these for your OS:

- [GCC](https://gcc.gnu.org/), the compiler the project is built with
- [premake5](https://premake.github.io/), which generates the build files

## Building and running (Linux)

The scripts use bash and make, so they only work on Linux:

```bash
scripts/linux/generate.sh   # generate the makefiles
scripts/linux/debug.sh      # generate, then build in debug configuration
scripts/linux/dev.sh        # run debug.sh, then run the binary
scripts/linux/release.sh    # generate, then build in release configuration (build/linux-x86_64/bin/release holds only the binary and its assets folder)
scripts/linux/clean.sh      # remove all generated and built files, including GLFW and GLEW
```

For day-to-day work `scripts/linux/dev.sh` is enough, also on a fresh checkout.
`debug.sh`, `dev.sh` and `release.sh` regenerate the makefiles on every run, so new
source files are picked up without running `generate.sh`. They do not remove any
objects or binaries, so only changed files are recompiled.

Only `clean.sh` removes everything, so GLFW and GLEW are rebuilt from scratch
after it.
