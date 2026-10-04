from core.font import draw_text
from core.lesson import Lesson

from pyray import BLACK, DARKBLUE, DARKGRAY


class LessonText:
    def draw(self, lesson: Lesson, number: int, total: int) -> None:
        draw_text(f"{number}/{total}  {lesson.title}", 20, 20, 30, BLACK)
        for i, line in enumerate(lesson.lines):
            draw_text(line, 20, 64 + i * 26, 20, DARKGRAY)
        draw_text(lesson.keys, 20, 76 + len(lesson.lines) * 26, 20, DARKBLUE)
