#pragma once

#include <string>

// Returns the directory that asset paths are resolved against.
//
// Debug: derived from the location of path.cpp (which lives in <project>/src).
// The build compiles sources by relative path, so this is an empty string
// and paths built from it only resolve when running from the project root.
//
// Release (Linux): the directory containing the executable, where the build
// copies the assets folder, so the binary runs from any working directory.
std::string project_dir();

// Returns `relative_path` joined onto the project root.
//
//   project_path("assets/shaders/basic.glsl")
std::string project_path(std::string relative_path);
