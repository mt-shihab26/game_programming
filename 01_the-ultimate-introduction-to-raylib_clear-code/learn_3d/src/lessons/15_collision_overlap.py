from pyray import draw_line_3d, draw_sphere
from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import V, Vec

from pyray import BLACK


class CollisionOverlapLesson(Lesson):
    title = "Which way out? The smallest overlap"
    lines = [
        "True or False is not enough to stop the player. You also need",
        "to know which side it came in from.",
        "Measure how deep the boxes overlap on each axis.",
        "The smallest one is the side it just crossed, and the shortest",
        "way back out. The black line shows that push.",
    ]
    keys = MOVE_KEYS
    code = ("overlap_x", "overlap_y", "overlap_z", "collision_axis")
    objects = ("player_box", "obstacle_box")

    def pushed_out(self) -> Vec | None:
        axis = self.scene.collision_axis
        if axis is None:
            return None
        player, obstacle = self.scene.player_box, self.scene.obstacle_box
        position = list(player.pos)
        position[axis] = player.pushed_out(obstacle, axis)
        return position

    def update(self, delta_time: float) -> None:
        player, obstacle = self.scene.player_box, self.scene.obstacle_box
        move(player.pos, delta_time)
        self.scene.collision_axis = player.push_axis(obstacle)
        obstacle.hit = self.scene.collision_axis is not None

    def draw(self) -> None:
        super().draw()
        pushed_out = self.pushed_out()
        if pushed_out is not None:
            draw_line_3d(V(self.scene.player_box.pos), V(pushed_out), BLACK)
            draw_sphere(V(pushed_out), 0.08, BLACK)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        pushed_out = self.pushed_out()
        if pushed_out is not None:
            name = "XYZ"[self.scene.collision_axis]
            label(f"push out on {name}", pushed_out, BLACK)
