from math import sqrt

from pyray import Vector3

Vec = list[float]


def V(v: Vec) -> Vector3:
    return Vector3(v[0], v[1], v[2])


def add(a: Vec, b: Vec) -> Vec:
    return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]


def sub(a: Vec, b: Vec) -> Vec:
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def scale(a: Vec, s: float) -> Vec:
    return [a[0] * s, a[1] * s, a[2] * s]


def cross(a: Vec, b: Vec) -> Vec:
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]


def length(a: Vec) -> float:
    return sqrt(a[0] * a[0] + a[1] * a[1] + a[2] * a[2])


def norm(a: Vec) -> Vec:
    l = length(a)
    return scale(a, 1 / l) if l > 0.0001 else [0, 0, 0]


def fmt(v: Vec) -> str:
    return f"Vector3({v[0]:.1f}, {v[1]:.1f}, {v[2]:.1f})"


def vec(v: Vector3) -> Vec:
    return [v.x, v.y, v.z]
