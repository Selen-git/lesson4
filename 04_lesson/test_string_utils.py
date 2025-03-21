class StringUtils:

    def capitalize(self, string: str) -> str:
       capitilize("skypro") -> "Skypro"
        return string.capitalize()

    def trim(self, string: str) -> str:
        trim("   skypro") -> "skypro"
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        string - строка для обработки
        symbol - искомый символ
        contains("SkyPro", "S") -> True
        contains("SkyPro", "U") -> False
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        delete_symbol("SkyPro", "k") -> "SyPro"
        delete_symbol("SkyPro", "Pro") -> "Sky"
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string



import string_utils.py from test_string_utils.py


@pytest.mark.parametrize('input_text, output_text', [
    ('Hello', 'Hello'),
    ('hello', 'Hello'),
    ('h', 'H'),
    ('привет', 'Привет')
    ])
def test_capitilize_positive(input_text, output_text):
    stringUtils = StringUtils()
    assert stringUtils.capitilize(input_text) == output_text



def test_to_list_with_delimiter_positive(input_text, delimiter, expected_output):
    strings = StringUtils()
    assert strings.to_list(input_text, delimiter) == expected_output




@pytest.mark.parametrize('list, output_list', [
    (["", "", "", ""], ",,,"),
    ([" ", " ", " ", " "], " , , , "),
    ])
def test_list_to_string_negative(list, output_list):
    stringUtils = StringUtils()
    assert stringUtils.list_to_string(list) == output_list




@pytest.fixture
def sample_data():
    return {"name": "Alice", "age": 30}

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
