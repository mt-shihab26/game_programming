from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = ROOT_DIR.joinpath("assets")
FONT_DIR = ASSETS_DIR.joinpath("fonts")
IMAGES_DIR = ASSETS_DIR.joinpath("images")
SOUNDS_DIR = ASSETS_DIR.joinpath("sounds")


def stormfaze_font_path() -> str:
    return str(FONT_DIR.joinpath("stormfaze.otf"))


def laser_image_path() -> str:
    return str(IMAGES_DIR.joinpath("laser.png"))


def meteor_image_path() -> str:
    return str(IMAGES_DIR.joinpath("meteor.png"))


def spaceship_image_path() -> str:
    return str(IMAGES_DIR.joinpath("spaceship.png"))


def star_image_path() -> str:
    return str(IMAGES_DIR.joinpath("star.png"))


def explosion_image_paths() -> list[str]:
    frames = sorted(
        IMAGES_DIR.joinpath("explosion").glob("*.png"), key=lambda p: int(p.stem)
    )
    return [str(frame) for frame in frames]


def explosion_sound_path() -> str:
    return str(SOUNDS_DIR.joinpath("explosion.wav"))


def laser_sound_path() -> str:
    return str(SOUNDS_DIR.joinpath("laser.wav"))


def music_sound_path() -> str:
    return str(SOUNDS_DIR.joinpath("music.wav"))
