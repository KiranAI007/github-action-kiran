from src.math_operation import add, sub

# define the test cases for add
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

# define the test cases for subtract
def test_sub():
    assert sub(5, 3) == 2
    assert sub(-2, 5) == -7
    