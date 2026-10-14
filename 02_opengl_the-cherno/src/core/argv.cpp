#include "argv.hpp"

Argv::Argv(int argc, char *i_argv[]) {
    for (int i = 0; i < argc; i++) {
        argv.push_back(i_argv[i]);
    }
}

bool Argv::empty() {
    // argv[0] is the program path, so arguments start at index 1
    return argv.size() < 2;
}

std::string Argv::first() {
    if (empty()) {
        return "";
    }
    return argv[1];
}
