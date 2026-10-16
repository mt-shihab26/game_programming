#type vertex

#version 330 core

layout(location = 0) in vec3 a_position;
layout(location = 2) in vec2 a_tex_coord;

out vec2 v_tex_coord;

uniform mat4 u_mvp;

void main()
{
    gl_Position = u_mvp * vec4(a_position, 1.0);
    v_tex_coord = a_tex_coord;
};

#type fragment

#version 330 core

in vec2 v_tex_coord;

layout(location = 0) out vec4 o_color;

uniform sampler2D u_texture;

void main()
{
    o_color = texture(u_texture, v_tex_coord);
};
