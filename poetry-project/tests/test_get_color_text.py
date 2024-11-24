import pytest # type: ignore
from unittest import mock
from ascii_art_project.main import AsciiArtGenerator


@pytest.fixture
def mock_args():
    class MockArgs:
        def __init__(self, banner="standard", color=None, letters=None, align=None, text="Hello", output=None):
            self.banner = banner
            self.color = color
            self.letters = letters
            self.align = align
            self.text = text
            self.output = output
    return MockArgs()

@pytest.fixture
def generator(mock_args):
    return AsciiArtGenerator(mock_args)



@pytest.mark.parametrize("color, letters, art_char, char, expected", [
    (None, None, "|", "a", "|"),

    ("red", None, "|", "a", "\033[31m|\033[0m"),

    ("red", "a", " / _` |", "a", "\033[31m / _` |\033[0m"),

    ("magenta", "F", "|  ____|", "b", "|  ____|"),

    ("cyan", "XtRo", "_|_|_|  ", "R", "\033[36m_|_|_|  \033[0m"),

    ("green", "Yzs}gm", "  O-o", "}", "\033[32m  O-o\033[0m"),

    ("yellow", "@#A!b[]", "o---o", "7", "o---o"),
])
def test_get_color_text_not_empty(color, letters, art_char, char, expected, generator):
    generator.args.color = color 
    generator.args.letters = letters 
    generator.color_code = generator.ANSI_COLOR_MAP.get(color, '')
    generator.colored_letters = set(letters) if letters else set()

    result = generator.get_color_text(art_char, char)
    assert result == expected


