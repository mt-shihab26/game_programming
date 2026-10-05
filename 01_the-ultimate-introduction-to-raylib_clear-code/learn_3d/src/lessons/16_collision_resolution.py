from core.controls import MOVE_KEYS, move

from core.lesson import Lesson


class CollisionResolutionLesson(Lesson):
    title = "Collision resolution"
    lines = [
        "Now the push happens every frame, so the player never gets in.",
        "It is put exactly touching: the obstacle's centre, plus or minus",
        "half of each box.",
        "The axis is picked once, when the boxes first touch, and kept",
        "until they part. That lets you slide along a wall.",
        "Rise with E, move over the grey box and drop with Q to land on top.",
    ]
    keys = MOVE_KEYS
    code = ("player_box.position", "collision_axis", "push_out")
    objects = ("player_box", "obstacle_box")

    def update(self, delta_time: float) -> None:
        player, obstacle = self.scene.player_box, self.scene.obstacle_box
        move(player.pos, delta_time)
        if not player.hits(obstacle):
            self.scene.collision_axis = None
        elif self.scene.collision_axis is None:
            self.scene.collision_axis = player.push_axis(obstacle)
        axis = self.scene.collision_axis
        if axis is not None:
            player.pos[axis] = player.pushed_out(obstacle, axis)
        obstacle.hit = axis is not None
