#type vertex

#version 460 core

layout(location = 0) in vec3 a_position;
layout(location = 2) in vec2 a_tex_coord;
layout(location = 3) in float a_tex_index;

out vec2 v_tex_coord;
out float v_tex_index;

uniform mat4 u_mvp;

void main()
{
    gl_Position = u_mvp * vec4(a_position, 1.0);
    v_tex_coord = a_tex_coord;
    v_tex_index = a_tex_index;
};

#type fragment

#version 460 core

in vec2 v_tex_coord;
in float v_tex_index;

layout(location = 0) out vec4 o_color;

uniform sampler2D u_texture[2];

void main()
{
    o_color = texture(u_texture[int(u_tex_index)], v_tex_coord);
};
