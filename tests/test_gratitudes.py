from lib.gratitudes import *

def test_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("food on your table")
    result = gratitudes.format()
    assert result == "Be grateful for: food on your table"

# class Gratitudes:
#     def __init__(self):
#         self.gratitudes = []

#     def add(self, gratitude):
#         self.gratitudes.append(gratitude)

#     def format(self):
#         formatted = "Be grateful for: "
#         formatted += ", ".join(self.gratitudes)
#         return formatted