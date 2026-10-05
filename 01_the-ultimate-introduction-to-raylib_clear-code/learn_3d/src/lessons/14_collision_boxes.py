from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import vec

from pyray import BLACK


class CollisionBoxesLesson(Lesson):
    title = "check_collision_boxes(box1, box2)"
    lines = [
        "Move the blue box into the grey one. It turns red on True.",
        "Two boxes touch only when they overlap on X and on Y and on Z.",
        "A gap on just one axis keeps them apart: lift the blue box",
        "over the grey one and Y has a gap, so it is False.",
    ]
    keys = MOVE_KEYS
    code = ("player_box.position", "obstacle_box.position", "check_collision_boxes")
    objects = ("player_box", "obstacle_box")

    def update(self, delta_time: float) -> None:
        player, obstacle = self.scene.player_box, self.scene.obstacle_box
        move(player.pos, delta_time)
        obstacle.hit = player.hits(obstacle)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        player = self.scene.player_box.bounding_box()
        obstacle = self.scene.obstacle_box.bounding_box()
        low, high = vec(player.min), vec(player.max)
        other_low, other_high = vec(obstacle.min), vec(obstacle.max)
        text = ""
        for i, name in enumerate("XYZ"):
            overlap = low[i] <= other_high[i] and high[i] >= other_low[i]
            text += f"{name}: {'overlap' if overlap else 'gap'}    "
        label(text, high, BLACK)
