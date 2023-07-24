from lib.greet import greet

def test_greet():
    assert greet('Kay') == 'Hello, Kay!'

def test_greet_jay():
    assert greet('Jay') == 'Hello, Jay!'