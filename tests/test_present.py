import pytest
from lib.present import *

def test_present():
    present = Present()
    with pytest.raises(Exception) as e:
        result = present.wrap('flower')
        assert result == "A contents has already been wrapped."

def test_present_for_none():
    present = Present()
    present.wrap(None)
    with pytest.raises(Exception) as e:
        result = present.unwrap()
        assert result == "No contents have been wrapped."