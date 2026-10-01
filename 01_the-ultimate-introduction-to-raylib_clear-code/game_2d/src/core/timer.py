from pyray import get_time

from collections.abc import Callable


class Timer:
    def __init__(
        self,
        duration: float,
        repeat=False,
        autostart=False,
        func: Callable[[], None] | None = None,
    ):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.repeat = repeat
        self.func = func
        self.previous_count = 0
        self.current_count = 0

        if autostart:
            self.start()

    def start(self):
        self.active = True
        self.start_time = get_time()

    def stop(self):
        self.active = False
        self.start_time = 0

    def update(self):
        if not self.active:
            return
        self.previous_count = 0
        self.current_count = 0
        if get_time() - self.start_time >= self.duration:
            self.previous_count = 0
            self.current_count += 1
            if self.func:
                self.func()
            self.stop()
            if self.repeat:
                self.start()

    def __repr__(self):
        return (
            f"Timer(duration={self.duration}, start_time={self.start_time}, "
            f"active={self.active}, repeat={self.repeat},"
            f"previous_count={self.previous_count}, current_count={self.current_count}"
        )
