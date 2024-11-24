import pytest # type: ignore
from unittest.mock import patch, mock_open, MagicMock
from ascii_art_project.main import AsciiArtGenerator


@pytest.fixture
def mock_args():
    class MockArgs:
        def __init__(self, text="", banner="standard", color=None, letters=None, align=None, output=None):
            self.text = text
            self.banner = banner
            self.color = color
            self.letters = letters
            self.align = align
            self.output = output
    return MockArgs()



@pytest.fixture
def generator(mock_args):
    generator = AsciiArtGenerator(mock_args)
    return generator



@pytest.mark.parametrize("text, color, letters, expected", [
    ("hello", None, None, "".join([' _              _   _          \n| |            | | | |         \n| |__     ___  | | | |   ___   \n|  _ \\   / _ \\ | | | |  / _ \\  \n| | | | |  __/ | | | | | (_) | \n|_| |_|  \\___| |_| |_|  \\___/  \n                               \n                               \n'])),

    ("Hello, world", None, None, "".join([" _    _          _   _                                               _       _  \n| |  | |        | | | |                                             | |     | | \n| |__| |   ___  | | | |   ___             __      __   ___    _ __  | |   __| | \n|  __  |  / _ \\ | | | |  / _ \\            \\ \\ /\\ / /  / _ \\  | '__| | |  / _` | \n| |  | | |  __/ | | | | | (_) |  _         \\ V  V /  | (_) | | |    | | | (_| | \n|_|  |_|  \\___| |_| |_|  \\___/  ( )         \\_/\\_/    \\___/  |_|    |_|  \\__,_| \n                                |/                                              \n                                                                                \n"])), 

    ("Hello, Hum@n\nAg4in :)", None, None, "".join([" _    _          _   _                     _    _                                        \n| |  | |        | | | |                   | |  | |                        ____           \n| |__| |   ___  | | | |   ___             | |__| |  _   _   _ __ ___     / __ \\   _ __   \n|  __  |  / _ \\ | | | |  / _ \\            |  __  | | | | | | '_ ` _ \\   / / _` | | '_ \\  \n| |  | | |  __/ | | | | | (_) |  _        | |  | | | |_| | | | | | | | | | (_| | | | | | \n|_|  |_|  \\___| |_| |_|  \\___/  ( )       |_|  |_|  \\__,_| |_| |_| |_|  \\ \\__,_| |_| |_| \n                                |/                                       \\____/          \n                                                                                         \n", "                             _                    __   \n    /\\              _  _    (_)                _  \\ \\  \n   /  \\      __ _  | || |    _   _ __         (_)  | | \n  / /\\ \\    / _` | | || |_  | | | '_ \\             | | \n / ____ \\  | (_| | |__   _| | | | | | |        _   | | \n/_/    \\_\\  \\__, |    |_|   |_| |_| |_|       (_)  | | \n             __/ |                                /_/  \n            |___/                                      \n"])), 

    ('nFactorial', "red", "Ftln", "".join(["\x1b[31m        \x1b[0m\x1b[31m ______  \x1b[0m               \x1b[31m _    \x1b[0m                _          \x1b[31m _  \n\x1b[0m\x1b[31m        \x1b[0m\x1b[31m|  ____| \x1b[0m               \x1b[31m| |   \x1b[0m               (_)         \x1b[31m| | \n\x1b[0m\x1b[31m _ __   \x1b[0m\x1b[31m| |__    \x1b[0m  __ _    ___  \x1b[31m| |_  \x1b[0m  ___    _ __   _    __ _  \x1b[31m| | \n\x1b[0m\x1b[31m| '_ \\  \x1b[0m\x1b[31m|  __|   \x1b[0m / _` |  / __| \x1b[31m| __| \x1b[0m / _ \\  | '__| | |  / _` | \x1b[31m| | \n\x1b[0m\x1b[31m| | | | \x1b[0m\x1b[31m| |      \x1b[0m| (_| | | (__  \x1b[31m\\ |_  \x1b[0m| (_) | | |    | | | (_| | \x1b[31m| | \n\x1b[0m\x1b[31m|_| |_| \x1b[0m\x1b[31m|_|      \x1b[0m \\__,_|  \\___| \x1b[31m \\__| \x1b[0m \\___/  |_|    |_|  \\__,_| \x1b[31m|_| \n\x1b[0m\x1b[31m        \x1b[0m\x1b[31m         \x1b[0m               \x1b[31m      \x1b[0m                           \x1b[31m    \n\x1b[0m\x1b[31m        \x1b[0m\x1b[31m         \x1b[0m               \x1b[31m      \x1b[0m                           \x1b[31m    \n\x1b[0m"]))

])
def test_process_text(text, color, letters, expected, mocker, generator):
    generator.args.text = text
    generator.args.color = color 
    generator.args.letters = letters 
    generator.load_ascii_art()
    generator.color_code = generator.ANSI_COLOR_MAP.get(generator.args.color, '')
    generator.colored_letters = set(generator.args.letters) if generator.args.letters else set()

    mock_stdout = mocker.patch("sys.stdout.write")
    mock_exit = mocker.patch("sys.exit")
    generator.process_text()

    result = "".join([call.args[0] for call in mock_stdout.call_args_list])
    assert result == expected
    mock_exit.assert_called_once_with(0)

