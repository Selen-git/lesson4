from String_utils import StringUtils


string_ut = StringUtils()




string_utils = StringUtils()

import pytest

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive1(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

def test_capitalize_positive():
    input_string = 'hello'
    expected_output = 'Hello'

    result = string_ut.capitalize(input_string)

    assert result == expected_output 

def test_capitalize_negative():
    input_string = 'World'
    expected_output = 'World'

    result = string_ut.capitalize(input_string)

    assert result == expected_output 






def test_trim_positive():
    input_string = 'example'
    expected_output = 'example'

    result = string_ut.trim(input_string)

    assert result == expected_output

def test_trim_negative():
    input_string = '  text'
    expected_output = 'text'

    result = string_ut.trim(input_string)

    assert result == expected_output





def test_contains_positive():
    input_string = 'hello'
    symbol = 'e'

    result = string_ut.contains(input_string, symbol)

    assert result == True

def test_contains_negative():
    input_string = 'world'
    symbol = 'a'

    result = string_ut.contains(input_string, symbol)

    assert result == False





def test_delete_symbol_positive():
    input_string = 'hello'
    symbol = 'l'
    expected_output = 'heo'

    result = string_ut.delete_symbol(input_string, symbol)

    assert result == expected_output

def test_delete_symbol_negative():
    input_string = 'world'
    symbol = 'x'

    result = string_ut.delete_symbol(input_string, symbol)

    assert result == input_string
