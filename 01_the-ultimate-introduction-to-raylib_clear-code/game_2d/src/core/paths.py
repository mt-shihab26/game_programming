from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

ASSETS_DIR = ROOT_DIR / "assets"
FONT_DIR = ASSETS_DIR / "fonts"
IMAGES_DIR = ASSETS_DIR / "images"
SOUNDS_DIR = ASSETS_DIR / "sounds"


def stormfaze_font_path() -> str:
    return str(FONT_DIR / "stormfaze.otf")


def laser_image_path() -> str:
    return str(IMAGES_DIR / "laser.png")


def meteor_image_path() -> str:
    return str(IMAGES_DIR / "meteor.png")


def spaceship_image_path() -> str:
    return str(IMAGES_DIR / "spaceship.png")


def star_image_path() -> str:
    return str(IMAGES_DIR / "star.png")


def explosion_image_paths() -> list[str]:
    frames = sorted((IMAGES_DIR / "explosion").glob("*.png"), key=lambda p: int(p.stem))
    return [str(frame) for frame in frames]


def explosion_sound_path() -> str:
    return str(SOUNDS_DIR / "explosion.wav")


def laser_sound_path() -> str:
    return str(SOUNDS_DIR / "laser.wav")


def music_sound_path() -> str:
    return str(SOUNDS_DIR / "music.wav")
