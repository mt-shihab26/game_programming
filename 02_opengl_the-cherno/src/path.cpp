#include <filesystem>
#include <string>

#if defined(_WIN32)
#include <windows.h>
#elif defined(__APPLE__)
#include <mach-o/dyld.h>
#endif

#include "path.hpp"

static std::filesystem::path executable_path() {
#if defined(_WIN32)
    wchar_t buffer[MAX_PATH];
    GetModuleFileNameW(nullptr, buffer, MAX_PATH);
    return buffer;
#elif defined(__APPLE__)
    char buffer[4096];
    uint32_t size = sizeof(buffer);
    _NSGetExecutablePath(buffer, &size);
    return std::filesystem::canonical(buffer);
#else
    return std::filesystem::canonical("/proc/self/exe");
#endif
}

std::string project_dir() {
#if defined(NDEBUG)
    // release: assets are copied next to the executable
    return executable_path().parent_path().string();
#else
    // this file lives in <project>/src
    return std::filesystem::path(__FILE__).parent_path().parent_path().string();
#endif
}

std::string project_path(std::string relative_path) {
    return (std::filesystem::path(project_dir()) / relative_path).string();
}
