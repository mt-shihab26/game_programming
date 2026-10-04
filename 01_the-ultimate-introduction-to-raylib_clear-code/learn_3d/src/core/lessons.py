MOVE_KEYS = "A/D: x    Q/E: y    W/S: z"

# (title, text lines, key hint), shown in this order
LESSONS = [
    (
        "A point is three numbers",
        [
            "Every position in 3D is Vector3(x, y, z).",
            "X = right (red), Y = up (green), Z = toward you (blue).",
            "Follow the path: walk x along red, z along blue, then climb y.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.position",
        [
            "Where your eye is in the world.",
            "The black ball is the camera. The small picture is what it sees.",
            "Move it and watch both views change.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.target",
        [
            "The point the camera looks at (pink ball).",
            "The camera stays where it is and turns to face it.",
        ],
        MOVE_KEYS,
    ),
    (
        "camera.fovy",
        [
            "How wide the lens is, in degrees.",
            "The blue pyramid is everything the camera can see.",
            "Wider angle: you see more, so things look smaller.",
        ],
        "W/S: fovy",
    ),
    (
        "camera.projection",
        [
            "PERSPECTIVE: far things look smaller (a pyramid).",
            "ORTHOGRAPHIC: size never changes with distance (a box).",
            "In orthographic, fovy is the view height in world units.",
        ],
        "SPACE: switch    W/S: fovy",
    ),
    (
        "camera.up",
        [
            "Up does not move the camera or change where it looks.",
            "It only says which side of the picture is the top.",
            "The green stick on the camera is up. The green edge is the",
            "top of the picture. Lean the stick and the picture leans too,",
            "like tilting your head sideways.",
            "Only the direction counts: (0, 1, 0) and (0, 10, 0) are the same.",
        ],
        MOVE_KEYS,
    ),
    (
        "draw_model(model, position, scale, tint)",
        [
            "position places the centre of the cube.",
            "At y = 0 half the cube is under the floor. y = 0.5 sits on it.",
        ],
        MOVE_KEYS + "    Z/X: scale",
    ),
    (
        "draw_line_3d(start, end, color): start",
        [
            "A line is just two points joined together.",
            "This lesson moves the first point (start).",
            "y = 0 keeps that end on the floor. Raise y and it lifts up.",
        ],
        MOVE_KEYS,
    ),
    (
        "draw_line_3d(start, end, color): end",
        [
            "Now move the second point (end).",
            "The line always runs straight between the two points,",
            "so moving one end swings and stretches the whole line.",
        ],
        MOVE_KEYS,
    ),
]
