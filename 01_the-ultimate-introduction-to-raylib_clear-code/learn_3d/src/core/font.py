from pathlib import Path
from subprocess import SubprocessError, run
from pyray import draw_text as draw_default_text
from pyray import draw_text_ex, is_font_valid, load_font_ex, trace_log, unload_font

from pyray import Color, Font, TraceLogLevel, Vector2

# one font per text size, so every size is drawn sharp. None = raylib's font
fonts: dict[int, Font | None] = {}


def system_font_file() -> str | None:
    # fontconfig knows which font the system uses for monospace text
    try:
        result = run(
            ["fc-match", "monospace", "--format=%{file}"],
            capture_output=True,
            text=True,
            timeout=2,
        )
    except (OSError, SubprocessError):
        return None
    file = result.stdout.strip()
    return file if result.returncode == 0 and Path(file).is_file() else None


def log(level: int, text: str) -> None:
    # trace_log reads % as a format marker
    trace_log(level, text.replace("%", "%%"))


def load_system_font(size: int) -> Font | None:
    file = system_font_file()
    if file is None:
        log(TraceLogLevel.LOG_WARNING, "FONT: no system font found, using raylib font")
        return None
    font = load_font_ex(file, size, None, 0)
    # a failed load hands back raylib's own font, which must not be unloaded
    if not is_font_valid(font) or font.glyphCount <= 0 or font.baseSize != size:
        log(TraceLogLevel.LOG_WARNING, f"FONT: could not load {file}, using raylib font")
        return None
    log(TraceLogLevel.LOG_INFO, f"FONT: system font loaded at size {size}: {file}")
    return font


def draw_text(text: str, x: int, y: int, size: int, color: Color) -> None:
    if size not in fonts:
        fonts[size] = load_system_font(size)
    font = fonts[size]
    if font is None:
        draw_default_text(text, x, y, size, color)
    else:
        draw_text_ex(font, text, Vector2(x, y), size, 0, color)


def unload_fonts() -> None:
    for font in fonts.values():
        if font is not None:
            unload_font(font)
    fonts.clear()
