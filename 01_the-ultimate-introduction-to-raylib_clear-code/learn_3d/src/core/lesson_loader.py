from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from core.lesson import Lesson

if TYPE_CHECKING:
    from entities.scene import Scene

LESSONS_DIR = Path(__file__).resolve().parent.parent.joinpath("lessons")


def lesson_number(file: Path) -> int:
    return int(file.stem.split("_")[0])


def load_lessons(scene: "Scene") -> list[Lesson]:
    # File names start with the lesson number (01_point.py), which sets the order.
    # A leading digit can't be written in an import statement, so load by name.
    lessons: list[Lesson] = []
    for file in sorted(LESSONS_DIR.glob("[0-9]*_*.py"), key=lesson_number):
        module = import_module(f"lessons.{file.stem}")
        for value in vars(module).values():
            if (
                isinstance(value, type)
                and issubclass(value, Lesson)
                and value.__module__ == module.__name__
            ):
                lessons.append(value(scene))
    return lessons
