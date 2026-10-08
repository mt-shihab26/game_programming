# 02_opengl_the-cherno

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
./scripts/generate.sh   # generate the makefiles (rerun after editing premake5.lua or adding source files)
./scripts/dev.sh        # build and run in debug configuration
./scripts/release.sh    # build in release configuration (bin/release holds only the binary and its assets folder)
./scripts/clean.sh      # remove all generated and built files
```
