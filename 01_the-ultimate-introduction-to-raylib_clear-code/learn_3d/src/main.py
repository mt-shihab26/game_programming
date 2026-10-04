from pyray import begin_drawing, begin_mode_3d, clear_background, close_window
from pyray import draw_grid, end_drawing, end_mode_3d, get_frame_time, init_window
from pyray import is_key_pressed, window_should_close
from core.controls import axis, move
from core.window import wait_for_window_size

from pyray import KeyboardKey
from core.vector import fmt
from entities.axes import Axes
from entities.cube import Cube
from entities.lesson_camera import LessonCamera
from entities.line import Line
from entities.observer import Observer
from entities.point import Point
from ui.code_panel import CodePanel
from ui.inset import Inset
from ui.lesson_text import LessonText

from pyray import BLACK, BLUE, DARKGREEN, MAROON, PURPLE, RAYWHITE, RED
from core.config import FOVY_SPEED, SCALE_SPEED, UP_SPEED
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH
from core.lessons import LESSONS


class App:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Learn 3D")
        wait_for_window_size()

        self.lesson = 0

        self.axes = Axes()
        self.point = Point()
        self.cube = Cube()
        self.line = Line()
        self.cam = LessonCamera()
        self.observer = Observer()

        self.inset = Inset()
        self.lesson_text = LessonText()
        self.code_panel = CodePanel(self.point, self.cam, self.cube, self.line)

    def show_camera(self) -> bool:
        return self.lesson > 0

    def line_end(self) -> str | None:
        # which end of the line the current lesson moves, if any
        return {7: "start", 8: "end"}.get(self.lesson)

    def reset(self) -> None:
        self.point.reset()
        self.cube.reset()
        self.line.reset()
        self.cam.reset()

    def close(self) -> None:
        self.cube.close()
        self.inset.close()
        close_window()

    def update(self, delta_time: float) -> None:
        if is_key_pressed(KeyboardKey.KEY_RIGHT):
            self.lesson = min(self.lesson + 1, len(LESSONS) - 1)
        if is_key_pressed(KeyboardKey.KEY_LEFT):
            self.lesson = max(self.lesson - 1, 0)
        if is_key_pressed(KeyboardKey.KEY_R):
            self.reset()
        if is_key_pressed(KeyboardKey.KEY_C):
            self.observer.reset()

        self.update_lesson(delta_time)
        self.cam.update(delta_time)
        self.observer.update(delta_time)

    def update_lesson(self, delta_time: float) -> None:
        if self.lesson == 0:
            move(self.point.pos, delta_time)
        elif self.lesson == 1:
            move(self.cam.pos, delta_time)
        elif self.lesson == 2:
            move(self.cam.target, delta_time)
        elif self.lesson in (3, 4):
            fovy = axis(KeyboardKey.KEY_W, KeyboardKey.KEY_S)
            self.cam.change_fovy(fovy * FOVY_SPEED * delta_time)
            if self.lesson == 4 and is_key_pressed(KeyboardKey.KEY_SPACE):
                self.cam.toggle_projection()
        elif self.lesson == 5:
            move(self.cam.up, delta_time, UP_SPEED)
        elif self.lesson == 6:
            move(self.cube.pos, delta_time)
            size = axis(KeyboardKey.KEY_X, KeyboardKey.KEY_Z)
            self.cube.resize(size * SCALE_SPEED * delta_time)
        elif self.lesson == 7:
            move(self.line.start, delta_time)
        elif self.lesson == 8:
            move(self.line.end, delta_time)

    def draw_scene(self) -> None:
        draw_grid(10, 1)
        self.axes.draw()
        self.cube.draw()
        self.line.draw()

    def draw_world(self) -> None:
        begin_mode_3d(self.observer.camera)
        self.draw_scene()
        if self.show_camera():
            self.cam.draw()
        else:
            self.point.draw()
        line_end = self.line_end()
        if line_end:
            self.line.draw_ends(line_end)
        end_mode_3d()

    def draw_labels(self) -> None:
        label = self.observer.label
        label("X", self.axes.x, RED)
        label("Y", self.axes.y, DARKGREEN)
        label("Z", self.axes.z, BLUE)
        if self.show_camera():
            label("camera.position", self.cam.pos, BLACK)
            label("camera.target", self.cam.target, MAROON)
            label("up", self.cam.up_tip(), DARKGREEN)
            label("top of picture", self.cam.picture_top, DARKGREEN)
        else:
            label(fmt(self.point.pos), self.point.pos, PURPLE)
        if self.line_end():
            label("start", self.line.start, MAROON)
            label("end", self.line.end, MAROON)

    def draw(self) -> None:
        if self.show_camera():
            self.inset.render(self.cam.camera, self.draw_scene)

        begin_drawing()
        clear_background(RAYWHITE)
        self.draw_world()
        self.draw_labels()
        self.lesson_text.draw(self.lesson)
        self.code_panel.draw(self.lesson)
        if self.show_camera():
            self.inset.draw()
        end_drawing()

    def run(self) -> None:
        while not window_should_close():
            delta_time = get_frame_time()
            self.update(delta_time)
            self.draw()
        self.close()


if __name__ == "__main__":
    App().run()
