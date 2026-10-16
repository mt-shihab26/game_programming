# OpenGL overview

A high-level map of how OpenGL works. The details of buffers and vertex arrays
are in `1-vertex-array-buffers-layout-index.md`, and the other concepts are in
`2-opengl-concepts.md`.

---

## 1. What OpenGL is

OpenGL is an **API specification**, not a library. Your GPU driver (Mesa,
NVIDIA, AMD) provides the implementation.

- **Loader (GLEW / glad):** fetches the function pointers from the driver when your program runs.
- **Windowing (GLFW / SDL):** creates the window and the OpenGL context, which the spec itself doesn't cover.

---

## 2. The mental model: a big state machine

OpenGL is a **global state machine** attached to a context. You don't pass
objects into functions. You **bind** an object to a target, and later calls act
on whatever is currently bound.

```cpp
glBindBuffer(GL_ARRAY_BUFFER, vbo);   // "select" it
glBufferData(GL_ARRAY_BUFFER, ...);   // acts on whatever is bound
```

This is why many bugs come down to "the wrong thing was bound", and why Cherno
wraps everything in classes with `Bind()` / `Unbind()`.

---

## 3. The CPU → GPU split

- **CPU (your C++):** prepares data, uploads it to GPU memory and issues commands.
- **GPU:** runs shaders in parallel over that data.
- **Asynchronous:** commands are queued. `glDraw*` returns right away, and the GPU does the work later.
- The main cost is often the **number of draw calls and state changes**, not the triangle count. This is the whole reason for batch rendering.

---

## 4. Core objects

| Object                       | Purpose                                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **VBO** (vertex buffer)      | Raw vertex data in GPU memory: positions, colors, UVs, texture IDs                                                      |
| **IBO / EBO** (index buffer) | Indices into the vertices so shared corners aren't duplicated (quad = 4 verts, 6 indices)                               |
| **VAO** (vertex array)       | Remembers the **layout** (`glVertexAttribPointer`) and which VBO/IBO go together. Bind the VAO and you're ready to draw |
| **Shader program**           | Linked vertex and fragment shaders (GLSL)                                                                               |
| **Texture**                  | Image data plus sampling settings, bound to numbered _texture slots_                                                    |
| **Framebuffer**              | A render target. The default one is the window; custom ones allow off-screen rendering                                  |
| **Uniform**                  | A per-draw constant sent to shaders (MVP matrix, color, sampler slots)                                                  |

---

## 5. The rendering pipeline

```
 Vertex data (VBO + layout in VAO)
        │
        ▼
 [Vertex Shader]       ← programmable: transforms each vertex (MVP matrix)
        │
 Primitive Assembly    ← groups vertices into triangles (using the index buffer)
        │
 Clipping + Perspective divide + Viewport transform
        │
 Rasterization         ← turns triangles into fragments (candidate pixels),
        │                interpolating vertex outputs across the triangle
        ▼
 [Fragment Shader]     ← programmable: computes each fragment's color
        │
 Per-fragment tests    ← depth test, stencil test, blending
        │
        ▼
 Framebuffer → swap buffers → screen
```

You write the two `[ ]` stages. Geometry and tessellation shaders are optional
stages after the vertex shader, and compute shaders run outside the pipeline.

---

## 6. Coordinate spaces (the MVP chain)

```
 Local ──Model──▶ World ──View──▶ Camera ──Projection──▶ Clip space
   ──(÷ w)──▶ NDC [-1, 1] ──viewport──▶ Screen pixels
```

- **Model:** where the object sits in the world (translate, rotate, scale).
- **View:** the inverse of the camera's transform.
- **Projection:** orthographic (2D) or perspective (3D).

In the vertex shader: `gl_Position = u_MVP * position;`, with glm building the
matrices. Multiplication runs right to left, so `MVP = P * V * M`.

---

## 7. A typical frame

```cpp
// setup (once)
// create VAO, VBO, IBO and set the layout; compile and link the shader; load textures

// every frame
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
shader.Bind();
shader.SetUniformMat4f("u_MVP", mvp);
texture.Bind(slot);
vao.Bind();
ibo.Bind();
glDrawElements(GL_TRIANGLES, count, GL_UNSIGNED_INT, nullptr);
glfwSwapBuffers(window);
glfwPollEvents();
```

---

## 8. Batch rendering

Instead of one draw call per quad (each with rebinds), draw many quads in **one** call:

1. Allocate one large **dynamic VBO** (`GL_DYNAMIC_DRAW`, `nullptr` data).
2. Each frame, write every quad's vertices into a CPU-side array. Pack per-vertex data such as color and a **texture index** into it.
3. Upload that array with `glBufferSubData`.
4. Generate the index buffer **once**: pattern `0,1,2, 2,3,0`, offset +4 per quad.
5. Bind up to N textures to slots `0..N-1` and pass a `sampler2D u_Textures[N]` array. The fragment shader picks one using the vertex's texture index.
6. Make **one** `glDrawElements` call. If the buffer or texture slots fill up, flush and start a new batch.

---

## 9. Other key concepts

- **Blending:** `glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);` for transparency.
- **Depth testing:** `glEnable(GL_DEPTH_TEST)` so nearer fragments win in 3D.
- **Errors:** `glGetError()` (Cherno's `GLCall` macro). GL 4.3+ has `glDebugMessageCallback`, which is much nicer.
- **Core vs compatibility profile:** core drops the old `glBegin`/`glEnd` API and **requires a bound VAO** to draw.
- **Versions:** 3.3 is the common modern baseline. 4.5 adds DSA (Direct State Access), e.g. `glNamedBufferData(buf, ...)`, which edits objects without binding them.

---

## 10. Where OpenGL sits today

OpenGL is still a good way to learn graphics, and it's widely supported. Its
successors are **Vulkan, DirectX 12 and Metal**. They're explicit, low-level APIs
with no hidden state machine, and you manage memory and synchronization yourself.
The concepts carry straight over: buffers, shaders, the pipeline, MVP and batching.
