# OpenGL concepts

The other concepts used in this project. Buffers and vertex arrays are in
`1-vertex-array-buffers-layout-index.md`.

---

## 1. OpenGL is a state machine

OpenGL keeps a set of **"current" things** (current vertex array, shader,
texture, blend mode…). Commands act on whatever is current.

```
 bind X   →  "X is now current"
 do stuff →  acts on X
 draw     →  uses everything current right now
```

- Objects are just **IDs** (numbers) that OpenGL gives you.
- Settings stay until you change them, so forgetting to reset something affects later draws.

---

## 2. A frame

```
 clear screen → for each object: bind + set uniforms → draw → show frame
```

"Show frame" swaps two images (**double buffering**): you draw into a hidden
one while the other is on screen, so you never see a half-drawn frame.

---

## 3. Shaders

A shader is **a small program that runs on the GPU**, written in GLSL.

| Shader              | Runs once per… | Job                                 |
| ------------------- | -------------- | ----------------------------------- |
| **Vertex shader**   | vertex         | **where** the corner goes on screen |
| **Fragment shader** | pixel          | **what color** the pixel is         |

```
 vertices ──▶ vertex shader ──▶ triangles filled in ──▶ fragment shader ──▶ pixels
```

Values passed from the vertex shader get blended across the triangle, so a
pixel halfway between two corners gets a value halfway between them.

Shaders are **compiled while your program runs**: compile vertex, compile
fragment, then **link** them into one **program**, which you bind before
drawing.

---

## 4. Uniforms

A **uniform** is a value that's **the same for the whole draw call**, set from
C++: a color, a matrix, a texture slot. Vertex data changes per vertex;
uniforms don't.

---

## 5. Textures

A texture is **an image uploaded to the GPU** that the fragment shader reads
colors from.

**Texture coordinates (UV)** say which part of the image goes on which
corner, from 0 to 1 regardless of image size:

```
 (0,1) ───── (1,1)
   │  image    │
 (0,0) ───── (1,0)
```

- **Flip on load:** images store rows top to bottom; OpenGL expects bottom to
  top. Without flipping, the image appears upside down.
- **Filtering:** `LINEAR` = smooth when scaled, `NEAREST` = blocky (pixel art).
- **Wrapping:** what happens outside 0..1. `CLAMP_TO_EDGE` stretches the
  edge, `REPEAT` tiles.
- **Slots:** the GPU has several texture slots (0, 1, 2…). Bind the texture
  to a slot, and tell the shader that slot number with a uniform.

---

## 6. Blending (transparency)

By default a new pixel **replaces** the old one, so transparent parts of a PNG
don't show what's behind them. Blending **mixes** them using alpha:

```
 result = new × alpha  +  old × (1 − alpha)
```

- Off by default; you turn it on.
- Draw things **behind first**, transparent things on top.

---

## 7. Model, View, Projection (MVP)

The GPU only draws what lands in a box from **−1 to 1**. Matrices convert
your coordinates into that box.

| Matrix         | Question                              |
| -------------- | ------------------------------------- |
| **Model**      | Where is this object?                 |
| **View**       | Where is the camera?                  |
| **Projection** | How does the world map to the screen? |

```
 object ─Model─▶ world ─View─▶ camera ─Projection─▶ screen (−1..1)
```

Combined as `MVP = P × V × M` (applied right to left) and sent to the vertex
shader as a uniform.

- **Orthographic** projection (what we use): no depth effect, good for 2D. We
  set 1 unit = 1 pixel.
- **Perspective:** far things look smaller, for 3D.

To move an object you don't change its vertices, you change its **model
matrix**. That's how the slider moves the quad.

---

## 8. Error checking

A failed OpenGL call **doesn't crash or return an error**. It sets an error
flag and continues. You have to ask with `glGetError`.

Our `GL_CALL` wrapper: clear old errors → run the call → check for new errors
→ print the call, file and line, then stop in the debugger. Without it, a
mistake usually means "nothing on screen" with no clue why.
