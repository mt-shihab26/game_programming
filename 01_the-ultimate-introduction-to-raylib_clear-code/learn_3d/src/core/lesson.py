from pyray import Color
from typing import TYPE_CHECKING, Callable
from core.vector import Vec

from pyray import BLACK, DARKGREEN, MAROON

if TYPE_CHECKING:
    from entities.scene import Scene

Label = Callable[[str, Vec, Color], None]


class Lesson:
    title: str = ""
    lines: list[str] = []
    keys: str = ""
    # names of the code panel lines this lesson changes
    highlights: tuple[str, ...] = ()
    # show the taught camera in the world and the picture it sees
    show_camera: bool = True
    # show the cube and the line, and their code. Off when a lesson wants
    # the floor to itself
    show_objects: bool = True

    def __init__(self, scene: "Scene") -> None:
        self.scene = scene

    def update(self, delta_time: float) -> None:
        pass

    def draw(self) -> None:
        # drawn in the world, on top of the scene
        if self.show_camera:
            self.scene.cam.draw()

    def draw_labels(self, label: Label) -> None:
        if self.show_camera:
            cam = self.scene.cam
            label("camera.position", cam.pos, BLACK)
            label("camera.target", cam.target, MAROON)
            label("up", cam.up_tip(), DARKGREEN)
            label("top of picture", cam.picture_top, DARKGREEN)
