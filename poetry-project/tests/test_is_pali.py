import pytest  # type: ignore
from is_pali import is_pali


@pytest.mark.parametrize("test_input, expected", [
    ("", True), 
    (" ", True), 
    ("   ", True),
    ("!", True),
    ("&%$", True),
    ("###", True),
])
def test_empty_string_returns_true(test_input, expected): 
    assert is_pali(test_input) == expected  



@pytest.mark.parametrize("test_input, expected", [
    ("a", True), 
    (" b", True), 
    ("   Y", True),
    ("@#$ g! ", True),
    ("0", True), 
    ("9", True),
    ("#a@", True), 
    ("__b__", True),
    ("(1)()", True),
    ("*:H# %", True), 
])
def test_one_alphanum_char_returns_true(test_input, expected): 
    assert is_pali(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [
    ("Bob", True), 
    ("rAcEcAr", True), 
    (" catatac  ", True),
    ("#Madam#", True),       
    ("!race%@car!", True),     
    ("no&on    ", True),         
    ("321de9ifi9ed123", True),        
    ("12345654321", True),         
    ("a*bc@cba^^", True),   
    ("helloworld", False), 
    ("Python", False), 
    ("deified123", False),    
    ("12345", False), 
    ("afauifhuaifhealufhaeihfailuildafhifalfhiefhealfha", False),
          
])
def test_is_pali_works_with_one_word(test_input, expected): 
    assert is_pali(test_input) == expected 



@pytest.mark.parametrize("test_input", [
    None, 
    False,
    123, 
    99.01, 
    1229447348317410846104317084,
    [], 
    [0,3],
    set(), 
    {3,99,-56,8},
])
def test_input_not_string_raises_exception(test_input):
    """
    Test that the function raises a TypeError for non-string inputs.
    """
    with pytest.raises(TypeError, match = "Input must be a string."):
        is_pali(test_input) 





