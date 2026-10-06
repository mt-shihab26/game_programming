-- stop: lsp

-- premake5.lua
workspace "demo"
configurations { "debug", "release" }

project "demo"
kind "ConsoleApp"
language "C++"
targetdir "bin/%{cfg.buildcfg}"

files { "src/**.h", "src/**.c", "src/**.cpp" }

filter "configurations:debug"
defines { "DEBUG" }
symbols "On"

filter "configurations:release"
defines { "NDEBUG" }
optimize "On"

newaction {
    trigger = "clean",
    description = "Remove generated build files",
    execute = function()
        os.rmdir("bin")
        os.rmdir("obj")
        os.remove("Makefile")
        os.remove("*.make")
    end
}
