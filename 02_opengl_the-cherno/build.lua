-- stop: lsp
-- stop: format

local build_dir = "build/%{cfg.system}-%{cfg.architecture}"
local bin_dir = build_dir .. "/bin/%{cfg.buildcfg}"
local obj_dir = build_dir .. "/obj/%{cfg.buildcfg}/%{prj.name}"
local wayland_dir = build_dir .. "/obj/wayland"

local function wayland_protocol_commands()
    local protocols = {
        "wayland",
        "viewporter",
        "xdg-shell",
        "idle-inhibit-unstable-v1",
        "pointer-constraints-unstable-v1",
        "relative-pointer-unstable-v1",
        "fractional-scale-v1",
        "xdg-activation-v1",
        "xdg-decoration-unstable-v1",
    }

    local commands = { "mkdir -p " .. wayland_dir }
    for _, name in ipairs(protocols) do
        local xml = "vendor/glfw/deps/wayland/" .. name .. ".xml"
        local header = wayland_dir .. "/" .. name .. "-client-protocol.h"
        local code = wayland_dir .. "/" .. name .. "-client-protocol-code.h"
        local scan = " || wayland-scanner "
        table.insert(commands, "[ -f " .. header .. " ]" .. scan .. "client-header " .. xml .. " " .. header)
        table.insert(commands, "[ -f " .. code .. " ]" .. scan .. "private-code " .. xml .. " " .. code)
    end
    return commands
end

workspace "demo"
    configurations { "debug", "release" }
    architecture "x86_64"
    toolset "clang"
    targetdir(bin_dir)
    objdir(obj_dir)

project "demo"
    kind "ConsoleApp"
    language "C++"

    files { "src/**.h", "src/**.cpp" }

    includedirs { "vendor/glfw/include", "vendor/glew/include" }
    defines { "GLEW_STATIC" }
    links { "glfw", "glew" }

    filter "system:linux"
        links {"GL", "EGL", "dl", "m", "pthread"}

    filter "system:windows"
        links { "opengl32", "gdi32" }

    filter "system:macosx"
        links { "Cocoa.framework", "IOKit.framework", "CoreVideo.framework", "OpenGL.framework" }

    filter "configurations:debug"
        defines { "DEBUG" }
        symbols "On"

    filter "configurations:release"
        defines { "NDEBUG" }
        optimize "On"
        postbuildcommands {
            "{RMDIR} %{cfg.targetdir}/assets",
            "{COPYDIR} assets %{cfg.targetdir}/assets",
            -- the static libraries are linked into the binary, so they are not needed to run it
            "{DELETE} %{cfg.targetdir}/libglfw.a",
            "{DELETE} %{cfg.targetdir}/libglew.a",
        }

project "glfw"
    kind "StaticLib"
    language "C"

    files {
        "vendor/glfw/src/context.c",
        "vendor/glfw/src/init.c",
        "vendor/glfw/src/input.c",
        "vendor/glfw/src/monitor.c",
        "vendor/glfw/src/platform.c",
        "vendor/glfw/src/vulkan.c",
        "vendor/glfw/src/window.c",
        "vendor/glfw/src/egl_context.c",
        "vendor/glfw/src/osmesa_context.c",
        "vendor/glfw/src/null_*.c",
    }

    filter "system:linux"
        defines { "_GLFW_WAYLAND", "HAVE_MEMFD_CREATE" }
        includedirs { wayland_dir }
        prebuildcommands(wayland_protocol_commands())
        files {
          "vendor/glfw/src/wl_*.c",
          "vendor/glfw/src/xkb_unicode.c",
          "vendor/glfw/src/posix_*.c",
          "vendor/glfw/src/linux_joystick.c",
        }

    filter "system:windows"
          defines { "_GLFW_WIN32" }
          files {
              "vendor/glfw/src/win32_*.c",
              "vendor/glfw/src/wgl_context.c",
          }

    filter "system:macosx"
        defines { "_GLFW_COCOA" }
        files {
          "vendor/glfw/src/cocoa_*.m",
          "vendor/glfw/src/nsgl_context.m",
          "vendor/glfw/src/macos_time.c",
          "vendor/glfw/src/posix_module.c",
          "vendor/glfw/src/posix_thread.c",
        }

    filter "configurations:debug"
        symbols "On"

    filter "configurations:release"
        optimize "On"

project "glew"
    kind "StaticLib"
    language "C"

    files { "vendor/glew/src/glew.c" }
    includedirs { "vendor/glew/include" }
    defines { "GLEW_STATIC", "GLEW_NO_GLU" }

    filter "system:linux"
        defines { "GLEW_EGL" }

    filter "configurations:debug"
        symbols "On"

    filter "configurations:release"
        optimize "On"

newaction {
    trigger = "clean",
    description = "Remove generated build files",
    execute = function()
        os.rmdir("build")
        os.remove("Makefile")
        os.remove("*.make")
    end
}
