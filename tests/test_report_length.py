from lib.report_length import report_length

def test_report_length():
    assert report_length("The best things in life are free!") == "This string was 33 characters long."

def test_report_length_1():
    assert report_length("Hello, World!") == "This string was 13 characters long."