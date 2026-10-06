from pyray import get_time

from collections.abc import Callable


class Timer:
    def __init__(
        self,
        duration: float,
        repeat=True,
        autostart=True,
        func: Callable[[], None] | None = None,
    ):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func

        if autostart:
            self.start()

    def start(self):
        self.active = True
        self.start_time = get_time()

    def stop(self):
        self.active = False
        self.start_time = 0

    def update(self) -> bool:
        if not self.active:
            return False
        if get_time() - self.start_time < self.duration:
            return False
        if self.func:
            self.func()
        self.stop()
        if self.repeat:
            self.start()
        return True

    def __repr__(self):
        return (
            f"Timer(duration={self.duration}, start_time={self.start_time}, "
            f"active={self.active}, repeat={self.repeat})"
        )
