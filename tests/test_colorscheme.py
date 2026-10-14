import configparser
from pathlib import Path

from deepwick_spec.check_port import check_port
from deepwick_spec.palette import ANSI_SLOTS, load_palette

REPO = Path(__file__).resolve().parents[1]
PALETTE = load_palette()
C = PALETTE.colors


def rgb(hex_: str) -> str:
    return ",".join(str(int(hex_[i : i + 2], 16)) for i in (1, 3, 5))


def scheme():
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    parser.read(REPO / "Deepwick.colorscheme", encoding="utf-8")
    assert parser.sections(), "Deepwick.colorscheme missing or empty"
    return parser


def test_general():
    general = scheme()["General"]
    assert general["Description"] == "Deepwick"
    assert general["Opacity"] == "1"


def test_background_and_foreground_variants():
    s = scheme()
    for variant in ("", "Faint", "Intense"):
        assert s[f"Background{variant}"]["Color"] == rgb(C["background"])
        assert s[f"Foreground{variant}"]["Color"] == rgb(C["foreground"])


def test_ansi_colors():
    s = scheme()
    for i, slot in enumerate(ANSI_SLOTS):
        normal = PALETTE.ansi[slot]
        bright = PALETTE.ansi["bright" + slot.capitalize()]
        assert s[f"Color{i}"]["Color"] == rgb(normal), slot
        assert s[f"Color{i}Faint"]["Color"] == rgb(normal), slot
        assert s[f"Color{i}Intense"]["Color"] == rgb(bright), slot


def test_port_conventions():
    assert check_port(REPO, PALETTE.allowed_hex()) == []
