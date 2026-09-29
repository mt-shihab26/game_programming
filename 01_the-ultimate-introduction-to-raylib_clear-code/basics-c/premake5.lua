workspace "basics"
configurations { "debug", "release" }

project "basics"
kind "ConsoleApp"
language "C"
targetdir "bin/%{cfg.buildcfg}"

files { "src/**.h", "src/**.c" }

filter "configurations:debug"
defines { "DEBUG" }
symbols "On"

filter "configurations:release"
defines { "NDEBUG" }
optimize "On"

newaction {
    trigger = "clean",
    description = "remove generated build files",
    execute = function()
        os.rmdir("obj")
        os.remove("Makefile")
        os.remove("*.make")
        print("done.")
    end,
}
