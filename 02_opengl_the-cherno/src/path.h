#pragma once

#include <string>

// Returns the project root directory, derived from the location of path.cpp (which lives in <project>/src).
//
// The build compiles sources by relative path, so this is an empty string
// and paths built from it only resolve when running from the project root.
std::string project_dir();

// Returns `relative_path` joined onto the project root.
//
//   project_path("assets/shaders/basic.glsl")
std::string project_path(std::string relative_path);
