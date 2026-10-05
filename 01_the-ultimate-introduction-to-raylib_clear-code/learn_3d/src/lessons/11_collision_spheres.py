from pyray import draw_line_3d
from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import V, add, length, scale, sub

from pyray import BLACK


class CollisionSpheresLesson(Lesson):
    title = "check_collision_spheres(center1, radius1, center2, radius2)"
    lines = [
        "Move the blue ball into the grey one. It turns red on True.",
        "The black line joins the two centres. Its length is the distance.",
        "Add the two radii together. If the distance is not bigger",
        "than that, the balls touch.",
    ]
    keys = MOVE_KEYS
    code = ("player_ball.position", "obstacle_ball.position", "check_collision_spheres")
    objects = ("player_ball", "obstacle_ball")

    def update(self, delta_time: float) -> None:
        player, obstacle = self.scene.player_ball, self.scene.obstacle_ball
        move(player.pos, delta_time)
        obstacle.hit = player.hits(obstacle)

    def draw(self) -> None:
        super().draw()
        player, obstacle = self.scene.player_ball, self.scene.obstacle_ball
        draw_line_3d(V(player.pos), V(obstacle.pos), BLACK)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        player, obstacle = self.scene.player_ball, self.scene.obstacle_ball
        distance = length(sub(obstacle.pos, player.pos))
        radii = player.radius + obstacle.radius
        middle = scale(add(player.pos, obstacle.pos), 0.5)
        label(f"distance {distance:.1f}    radii {radii:.1f}", middle, BLACK)
