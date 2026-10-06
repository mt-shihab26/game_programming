-- premake5.lua
workspace "Demo"
configurations { "Debug", "Release" }

project "Demo"
kind "ConsoleApp"
language "C++"
targetdir "bin/%{cfg.buildcfg}"

files { "src/**.h", "src/**.c", "src/**.cpp" }

filter "configurations:Debug"
defines { "DEBUG" }
symbols "On"

filter "configurations:Release"
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
