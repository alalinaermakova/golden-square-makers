from lib.string_builder import *

def test_string_builder():
    string_builder = StringBuilder()
    string_builder.add('Hello, Alina')
    result = string_builder.size()
    assert result == 12
    result1 = string_builder.output()
    assert result1 == 'Hello, Alina'

# class StringBuilder:
#     def __init__(self):
#         self.str = ""

#     def add(self, str):
#         self.str += str

#     def size(self):
#         return len(self.str)

#     def output(self):
#         return self.str