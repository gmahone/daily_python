def get_char(c):
  return chr(c)

# lambda version
get_char = lambda c: chr(c)




# add test
import unittest
   
class TestGetChar(unittest.TestCase):
    def test_get_char_return_A_when_given_65(self):
        self.assertEqual(get_char(65), 'A')
