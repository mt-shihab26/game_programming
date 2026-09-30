from collections.abc import Callable

from pyray import get_time


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
        if get_time() - self.start_time >= self.duration:
            if self.func:
                self.func()
            self.stop()
            if self.repeat:
                self.start()
