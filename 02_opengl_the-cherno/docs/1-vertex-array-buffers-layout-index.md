# Vertex Buffer, Layout, Vertex Array, Index Buffer — the concepts

## The problem they solve

You want the GPU to draw a shape. The GPU is a separate machine with its own
memory. It can't see your program's variables, and it doesn't know what your
data means. So you have to answer four questions for it:

| Question                                           | Answered by          |
| -------------------------------------------------- | -------------------- |
| **What** is the data?                              | Vertex Buffer        |
| **How** do I read it?                              | Vertex Buffer Layout |
| How do I **not repeat** all that setup every time? | Vertex Array         |
| **Which points** connect into triangles?           | Index Buffer         |

---

## First: what is a vertex?

A vertex is **one corner of a shape, plus everything you know about that
corner**: where it is, what color it is, which part of a texture it shows,
which way it faces, and so on.

So a vertex is not "a position". It's a small **record**, like a row in a
spreadsheet:

| corner | x   | y   | u   | v   |
| ------ | --- | --- | --- | --- |
| 0      | -50 | -50 | 0   | 0   |
| 1      | 50  | -50 | 1   | 0   |
| 2      | 50  | 50  | 1   | 1   |
| 3      | -50 | 50  | 0   | 1   |

Each column (position, texture coordinate, color…) is called an **attribute**.

---

## 1. Vertex Buffer: the data itself

A vertex buffer is **a chunk of GPU memory holding all your vertices, packed
one after another**.

The key idea: **the GPU only sees bytes.** The spreadsheet above turns into one
long row of numbers with no headers:

```
-50 -50 0 0 50 -50 1 0 50 50 1 1 -50 50 0 1
```

The GPU has no idea where one vertex ends and the next begins, or which number
is a position and which is a color. That's a problem the next piece solves.

> Analogy: a vertex buffer is a **box of numbers with no label on it**.

---

## 2. Vertex Buffer Layout: the label on the box

The layout **describes the shape of one vertex**:

> "Each vertex is: 2 numbers for position, then 2 numbers for texture coordinate."

From that description, two facts follow:

- **Stride:** how big one whole vertex is. To get to the next vertex, jump this far.
- **Offset:** where each attribute starts inside a vertex.

```
 one vertex
 ┌─────────────┬─────────────┐
 │  position   │  tex coord  │
 └─────────────┴─────────────┘
 ▲             ▲
 offset 0      offset 8 bytes

 ◀────── stride (16 bytes) ──────▶ then the next vertex starts
```

Each attribute also gets a **number (0, 1, 2…)**. The shader uses the same
numbers to say "give me attribute 0 as `position`, attribute 1 as `tex_coord`".
That number is the link between your data and your shader.

> Analogy: the layout is **the label on the box** that says
> "every 4 numbers is one item: the first 2 are X/Y, the next 2 are U/V."

(In OpenGL itself there's no "layout object". It's just a convenient way to
collect this description before handing it to OpenGL. The OpenGL call that
receives it is `glVertexAttribPointer`.)

---

## 3. Vertex Array: a saved setup

To draw, OpenGL needs to know all of this at the same moment:

- which buffer the vertices come from
- the layout (attributes, stride, offsets)
- which index buffer to use

Setting all that up before every draw would be tedious and slow. A
**Vertex Array (VAO) is a saved snapshot of that setup.** You configure it
once, and later just say "use that one", and everything comes back.

> Analogy: a **preset** or **save slot**. Like a saved profile in a game:
> instead of re-entering every setting each time, you load the profile.

If you have 10 different objects (a player, a tree, a rock…), you make 10 VAOs.
To switch what you're drawing, you switch the VAO.

```
 VAO "quad"
 ├── attribute 0 → read from Vertex Buffer A, 2 floats, offset 0, stride 16
 ├── attribute 1 → read from Vertex Buffer A, 2 floats, offset 8, stride 16
 └── index buffer → Index Buffer A
```

---

## 4. Index Buffer: reusing corners

GPUs draw **triangles**. A square is 2 triangles, which means 6 corners.
But a square only has **4 unique corners**. Two of them are shared.

```
 3 ───── 2
 │     ╱ │      triangle 1: 0 → 1 → 2
 │   ╱   │      triangle 2: 2 → 3 → 0
 │ ╱     │
 0 ───── 1      corners 0 and 2 are used twice
```

**Without** an index buffer you'd store 6 vertices, duplicating 2 of them.

**With** an index buffer you store the 4 unique vertices once, plus a short
list saying which ones to connect:

```
0, 1, 2,   2, 3, 0
```

> Analogy: **connect-the-dots**. The vertex buffer is the dots; the index
> buffer is the order to connect them.

Why it matters: for a square you save 2 vertices, which is nothing. But in a
real 3D model each corner is shared by around 6 triangles, so you save a lot
of memory. The GPU also skips recomputing a corner it has just processed.

---

## 5. Many vertex arrays, one bound at a time

You can create many vertex arrays (one per object), but only **one is bound
at a time**. A draw call renders whatever is bound right now: the vertex
array, and also the shader and texture.

```
bind VAO 1 → draw   (player)
bind VAO 2 → draw   (tree)
```

> Analogy: TV channels. Many saved, one on screen.

---

## How they fit together

```
     Vertex Buffer            Index Buffer
   (the dots: data)        (connect-the-dots order)
           │                        │
           │  + Layout              │
           │  (how to read a dot)   │
           ▼                        ▼
   ┌──────────────── Vertex Array ───────────────┐
   │  saved setup: "read these dots like this,   │
   │  connect them in this order"                │
   └─────────────────────┬───────────────────────┘
                         ▼
               Draw: "use this setup + this shader"
                         ▼
          GPU: for each index → fetch that vertex →
          split it into attributes using the layout →
          give them to the shader → build triangles → pixels
```

## One-line summary

- **Vertex Buffer:** the data (a box of numbers)
- **Layout:** how to interpret the data (the label on the box)
- **Vertex Array:** remembers buffer + layout + indices together (a save slot)
- **Index Buffer:** which vertices form triangles, so shared corners aren't duplicated (connect-the-dots)
- **Draw:** renders whatever is bound right now. You can have many vertex arrays, but only one is active at a time (TV channels)
