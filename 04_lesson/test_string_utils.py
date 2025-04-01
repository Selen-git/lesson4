from string_utils import StringUtils


def test_capitalize_positive(self):
    input_string = 'hello'
    expected_output = 'Hello'

    result = self.capitalize(input_string)

    self.assertEqual(result, expected_output) 

def test_capitalize_negative(self):
    input_string = 'World'
    expected_output = 'World'

    result = self.capitalize(input_string)

    self.assertNotEqual(result, expected_output)





def test_trim_positive(self):
    input_string = '  example  '
    expected_output = 'example'

    result = self.trim(input_string)

    self.assertEqual(result, expected_output)

def test_trim_negative(self):
    input_string = 'text'
    expected_output = 'text'

    result = self.trim(input_string)

    self.assertNotEqual(result, expected_output)





def test_contains_positive(self):
    input_string = 'hello'
    symbol = 'e'

    result = self.contains(input_string, symbol)

    self.assertTrue(result)

def test_contains_negative(self):
    input_string = 'world'
    symbol = 'a'

    result = self.contains(input_string, symbol)

    self.assertFalse(result)





def test_delete_symbol_positive(self):
    input_string = 'hello'
    symbol = 'l'
    expected_output = 'heo'

    result = self.delete_symbol(input_string, symbol)

    self.assertEqual(result, expected_output)

def test_delete_symbol_negative(self):
    input_string = 'world'
    symbol = 'x'

    result = self.delete_symbol(input_string, symbol)

    self.assertNotEqual(result, input_string)


















