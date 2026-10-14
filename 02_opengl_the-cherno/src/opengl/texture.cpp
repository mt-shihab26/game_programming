#include <string>

#include <glew/GL/glew.h>
#define STB_IMAGE_IMPLEMENTATION
#include <stb/stb_image.h>

#include "core/path.hpp"

#include "helper.hpp"

#include "texture.hpp"

Texture::Texture(const std::string &path) : m_renderer_id(0), m_filepath(path), m_local_buffer(nullptr), m_width(0), m_height(0), m_bpp(0) {
    stbi_set_flip_vertically_on_load(1);
    m_local_buffer = stbi_load(project_path(path).c_str(), &m_width, &m_height, &m_bpp, 4);

    GL_CALL(glGenTextures(1, &m_renderer_id));

    GL_CALL(glBindTexture(GL_TEXTURE_2D, m_renderer_id));

    GL_CALL(glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR));
    GL_CALL(glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR));
    GL_CALL(glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE));
    GL_CALL(glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE));

    GL_CALL(glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA8, m_width, m_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, m_local_buffer));

    GL_CALL(glBindTexture(GL_TEXTURE_2D, 0));

    if (m_local_buffer) {
        stbi_image_free(m_local_buffer);
    }
}

Texture::~Texture() {
    GL_CALL(glDeleteTextures(1, &m_renderer_id));
}

void Texture::bind(unsigned int slot) const {
    GL_CALL(glActiveTexture(GL_TEXTURE0 + slot));
    GL_CALL(glBindTexture(GL_TEXTURE_2D, m_renderer_id));
}

void Texture::unbind() const {
    GL_CALL(glBindTexture(GL_TEXTURE_2D, 0));
}
