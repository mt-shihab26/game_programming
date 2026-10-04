from pyray import begin_drawing, begin_mode_3d, clear_background, close_window
from pyray import end_drawing, end_mode_3d, get_frame_time, init_window
from pyray import is_key_pressed, window_should_close
from core.lesson_loader import load_lessons
from core.window import wait_for_window_size

from pyray import KeyboardKey
from core.lesson import Lesson
from entities.observer import Observer
from entities.scene import Scene
from ui.code_panel import CodePanel
from ui.inset import Inset
from ui.lesson_text import LessonText

from pyray import BLUE, DARKGREEN, RAYWHITE, RED
from core.config import WINDOW_HEIGHT, WINDOW_WIDTH


class App:
    def __init__(self) -> None:
        init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "Learn 3D")
        wait_for_window_size()

        self.scene = Scene()
        self.observer = Observer()

        self.lessons = load_lessons(self.scene)
        self.index = 0

        self.inset = Inset()
        self.lesson_text = LessonText()
        self.code_panel = CodePanel(self.scene)

    def lesson(self) -> Lesson:
        return self.lessons[self.index]

    def close(self) -> None:
        self.scene.close()
        self.inset.close()
        close_window()

    def update(self, delta_time: float) -> None:
        if is_key_pressed(KeyboardKey.KEY_RIGHT):
            self.index = min(self.index + 1, len(self.lessons) - 1)
        if is_key_pressed(KeyboardKey.KEY_LEFT):
            self.index = max(self.index - 1, 0)
        if is_key_pressed(KeyboardKey.KEY_R):
            self.scene.reset()
        if is_key_pressed(KeyboardKey.KEY_C):
            self.observer.reset()

        self.lesson().update(delta_time)
        self.scene.update(delta_time)
        self.observer.update(delta_time)

    def draw_world(self) -> None:
        begin_mode_3d(self.observer.camera)
        self.scene.draw()
        self.lesson().draw()
        end_mode_3d()

    def draw_labels(self) -> None:
        label = self.observer.label
        label("X", self.scene.axes.x, RED)
        label("Y", self.scene.axes.y, DARKGREEN)
        label("Z", self.scene.axes.z, BLUE)
        self.lesson().draw_labels(label)

    def draw(self) -> None:
        lesson = self.lesson()
        if lesson.show_camera:
            self.inset.render(self.scene.cam.camera, self.scene.draw)

        begin_drawing()
        clear_background(RAYWHITE)
        self.draw_world()
        self.draw_labels()
        self.lesson_text.draw(lesson, self.index + 1, len(self.lessons))
        self.code_panel.draw(lesson)
        if lesson.show_camera:
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
