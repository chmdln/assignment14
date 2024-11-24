import os 
import pytest # type: ignore
from ascii_art_project.main import AsciiArtGenerator


@pytest.fixture(autouse=True)
def set_cwd():
    original_cwd = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../")
    yield
    os.chdir(original_cwd)


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



def test_load_ascii_art_standard(mocker, generator):
    """
    Test load_ascii_art with "standard.txt" banner.
    """

    mock_content = "".join(['\n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '\n', ' _  \n', '| | \n', '| | \n', '| | \n', '|_| \n', '(_) \n', '    \n', '    \n', '\n', ' _ _  \n', '( | ) \n', ' V V  \n', '      \n', '      \n', '      \n', '      \n', '      \n', '\n', '   _  _    \n', ' _| || |_  \n', '|_  __  _| \n', ' _| || |_  \n', '|_  __  _| \n', '  |_||_|   \n', '           \n', '           \n', '\n'])

    expected = {" ": ['      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n'],
                "!": [' _  \n', '| | \n', '| | \n', '| | \n', '|_| \n', '(_) \n', '    \n', '    \n'], 
                "\"": [' _ _  \n', '( | ) \n', ' V V  \n', '      \n', '      \n', '      \n', '      \n', '      \n'], 
                "#": ['   _  _    \n', ' _| || |_  \n', '|_  __  _| \n', ' _| || |_  \n', '|_  __  _| \n', '  |_||_|   \n', '           \n', '           \n']}
    
    mock_open = mocker.mock_open(read_data=mock_content)
    mocker.patch("builtins.open", mock_open) 
    ascii_dict = generator.load_ascii_art()

    mock_open.assert_called_once_with("./ascii_art_project/data/standard.txt", "r")
    assert len(ascii_dict) == len(expected) 
    assert all(len(ascii_dict[char]) == 8 for char in ascii_dict.keys()) == True 
    assert ascii_dict == expected 



def test_load_ascii_art_shadow(mocker, generator):
    """
    Test load_ascii_art with "shadow.txt" banner.
    """

    generator.args.banner = "shadow"
    mock_content = "".join(['\n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '\n', '   \n', '_| \n', '_| \n', '_| \n', '   \n', '_| \n', '   \n', '   \n', '\n', '_|  _| \n', '_|  _| \n', '       \n', '       \n', '       \n', '       \n', '       \n', '       \n', '\n', '           \n', '  _|  _|   \n', '_|_|_|_|_| \n', '  _|  _|   \n', '_|_|_|_|_| \n', '  _|  _|   \n', '           \n', '           \n', '\n'])

    expected = {" ": ['      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n'],
                "!": ['   \n', '_| \n', '_| \n', '_| \n', '   \n', '_| \n', '   \n', '   \n'], 
                "\"": ['_|  _| \n', '_|  _| \n', '       \n', '       \n', '       \n', '       \n', '       \n', '       \n'], 
                "#": ['           \n', '  _|  _|   \n', '_|_|_|_|_| \n', '  _|  _|   \n', '_|_|_|_|_| \n', '  _|  _|   \n', '           \n', '           \n']}
    
    mock_open = mocker.mock_open(read_data=mock_content)
    mocker.patch("builtins.open", mock_open) 
    ascii_dict = generator.load_ascii_art()

    mock_open.assert_called_once_with("./ascii_art_project/data/shadow.txt", "r")
    assert len(ascii_dict) == len(expected) 
    assert all(len(ascii_dict[char]) == 8 for char in ascii_dict.keys()) == True 
    assert ascii_dict == expected 




def test_load_ascii_art_thinkertoy(mocker, generator):
    """
    Test load_ascii_art with "thinkertoy.txt" banner.
    """

    generator.args.banner = "thinkertoy"
    mock_content = "".join(['\n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '\n', '  \n', 'o \n', '| \n', 'o \n', '  \n', 'O \n', '  \n', '  \n', '\n', 'o o \n', '| | \n', '    \n', '    \n', '    \n', '    \n', '    \n', '    \n', '\n', '      \n', ' | |  \n', '-O-O- \n', ' | |  \n', '-O-O- \n', ' | |  \n', '      \n', '      \n', '\n'])

    expected = {" ": ['      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n', '      \n'],
                "!": ['  \n', 'o \n', '| \n', 'o \n', '  \n', 'O \n', '  \n', '  \n'], 
                "\"": ['o o \n', '| | \n', '    \n', '    \n', '    \n', '    \n', '    \n', '    \n'], 
                "#": ['      \n', ' | |  \n', '-O-O- \n', ' | |  \n', '-O-O- \n', ' | |  \n', '      \n', '      \n']}
    
    mock_open = mocker.mock_open(read_data=mock_content)
    mocker.patch("builtins.open", mock_open) 
    ascii_dict = generator.load_ascii_art()

    mock_open.assert_called_once_with("./ascii_art_project/data/thinkertoy.txt", "r")
    assert len(ascii_dict) == len(expected) 
    assert all(len(ascii_dict[char]) == 8 for char in ascii_dict.keys()) == True 
    assert ascii_dict == expected 



