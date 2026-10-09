# 02_opengl_the-cherno

## Installing the compiler

The project is built with [Clang](https://clang.llvm.org/) (set by `toolset "clang"` in `build.lua`).

Arch Linux:

```bash
sudo pacman -S clang
```

macOS: Clang comes with the Xcode command line tools:

```bash
xcode-select --install
```

Check that it works:

```bash
clang++ --version
```

## Installing premake

The build files are generated with [premake5](https://premake.github.io/).

Arch Linux:

```bash
sudo pacman -S premake
```

macOS:

```bash
brew install premake
```

Other Linux distros and Windows: download the `premake5` binary from
<https://premake.github.io/download> and put it somewhere on your `PATH`.

Check that it works:

```bash
premake5 --version
```

## Building and running (Linux)

The scripts use bash and make, so they only work on Linux:

```bash
./scripts/generate.sh   # generate the makefiles (rerun after editing build.lua or adding source files)
./scripts/dev.sh        # build and run in debug configuration
./scripts/release.sh    # build in release configuration (build/<os>-<arch>/bin/release holds only the binary and its assets folder)
./scripts/clean.sh      # remove all generated and built files
```
