from pyray import draw_line_3d, draw_sphere
from core.controls import MOVE_KEYS, move

from core.lesson import Label, Lesson
from core.vector import V, Vec, length, sub, vec

from pyray import BLACK


class CollisionBoxSphereLesson(Lesson):
    title = "check_collision_box_sphere(box, center, radius)"
    lines = [
        "Move the blue box into the grey ball. It turns red on True.",
        "The black dot is the point of the box nearest to the ball's centre.",
        "If that point is closer than the radius, the box is inside the ball.",
    ]
    keys = MOVE_KEYS
    code = (
        "player_box.position",
        "obstacle_ball.position",
        "check_collision_box_sphere",
    )
    objects = ("player_box", "obstacle_ball")

    def nearest(self) -> Vec:
        # the ball's centre, pulled back inside the box on each axis
        box = self.scene.player_box.bounding_box()
        low, high = vec(box.min), vec(box.max)
        center = self.scene.obstacle_ball.pos
        return [max(low[i], min(center[i], high[i])) for i in range(3)]

    def update(self, delta_time: float) -> None:
        player, obstacle = self.scene.player_box, self.scene.obstacle_ball
        move(player.pos, delta_time)
        obstacle.hit = player.hits_ball(obstacle)

    def draw(self) -> None:
        super().draw()
        nearest = self.nearest()
        draw_line_3d(V(nearest), V(self.scene.obstacle_ball.pos), BLACK)
        draw_sphere(V(nearest), 0.08, BLACK)

    def draw_labels(self, label: Label) -> None:
        super().draw_labels(label)
        obstacle = self.scene.obstacle_ball
        nearest = self.nearest()
        distance = length(sub(obstacle.pos, nearest))
        label(
            f"distance {distance:.1f}    radius {obstacle.radius:.1f}", nearest, BLACK
        )
