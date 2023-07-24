import pytest
from lib.password_checker import *

def test_password_checker():
    checker = PasswordChecker()
    result = checker.check('43789009e8!')
    assert result == True

def test_password_checker_invalid():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        result = checker.check('4009e8!')
        assert result == "Invalid password, must be 8+ characters."