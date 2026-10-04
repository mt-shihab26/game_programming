from pyray import begin_mode_3d, begin_texture_mode, clear_background
from pyray import draw_rectangle, draw_rectangle_lines, draw_texture_rec
from pyray import end_mode_3d, end_texture_mode, get_screen_width
from pyray import load_render_texture, unload_render_texture

from pyray import Camera3D, Rectangle, Vector2
from typing import Callable

from pyray import BLACK, DARKGREEN, LIME, WHITE
from core.font import draw_text
from core.config import INSET_HEIGHT, INSET_WIDTH


class Inset:
    """The small picture: what the taught camera sees."""

    def __init__(self) -> None:
        self.target = load_render_texture(INSET_WIDTH, INSET_HEIGHT)

    def close(self) -> None:
        unload_render_texture(self.target)

    def render(self, camera: Camera3D, draw_scene: Callable[[], None]) -> None:
        begin_texture_mode(self.target)
        clear_background(WHITE)
        begin_mode_3d(camera)
        draw_scene()
        end_mode_3d()
        end_texture_mode()

    def draw(self) -> None:
        x, y = get_screen_width() - INSET_WIDTH - 20, 44
        draw_text("What this camera sees", x, y - 24, 18, BLACK)
        draw_text("top", x + INSET_WIDTH - 34, y - 24, 18, DARKGREEN)
        draw_texture_rec(
            self.target.texture,
            Rectangle(0, 0, INSET_WIDTH, -INSET_HEIGHT),
            Vector2(x, y),
            WHITE,
        )
        draw_rectangle_lines(x - 1, y - 1, INSET_WIDTH + 2, INSET_HEIGHT + 2, BLACK)
        draw_rectangle(x - 1, y - 4, INSET_WIDTH + 2, 4, LIME)
