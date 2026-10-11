#type vertex

#version 330 core

layout(location = 0) in vec4 position;
layout(location = 1) in vec2 texCoord;

out vec2 v_tex_coord;

void main()
{
    gl_Position = position;
    v_tex_coord = texCoord;
};

#type fragment

#version 330 core

layout(location = 0) out vec4 color;

in vec2 v_tex_coord;

uniform vec4 u_color;
uniform sampler2D u_texture;

void main()
{
    vec4 texColor = texture(u_texture, v_tex_coord);
    color = texColor;
};
