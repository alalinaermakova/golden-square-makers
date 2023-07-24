from lib.check_codeword import check_codeword

def test_check_codeword():
    assert check_codeword('bubble') == "WRONG!"

def test_check_codeword_1():
    assert check_codeword('hole') == "Close, but nope."

def test_check_codeword_2():
    assert check_codeword('horse') == "Correct! Come in."