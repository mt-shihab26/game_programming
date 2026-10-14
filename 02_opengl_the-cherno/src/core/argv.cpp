#include "argv.hpp"

Argv::Argv(int argc, char *i_argv[]) {
    for (int i = 0; i < argc; i++) {
        argv.push_back(i_argv[i]);
    }
}

bool Argv::empty() {
    return argv.size() == 1;
}
std::string Argv::first() {
    if (empty()) {
        return "";
    }
    return argv[2];
}
