import sweets_chatgpt as s

sweets_list = [3, 10, 12, 16, 5]

def test_example():
    assert 1 == 1
    assert 1 != 2

def test_sweets_chatgpt():
    assert s.max_sweets_chatgpt(5, sweets_list) == 26

def test_sweets_class():
    assert s.max_sweets_class(sweets_list) == 26
