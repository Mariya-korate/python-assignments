#Assignment 2
# Check that two separate lists are NOT the same object
import pytest


def test_list_obj():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert id(a) != id(b)

# Check if an element is NOT present in a list
def test_ele_not_in_list():
    a = [1, 2, 3]
    assert 5 not in a

# Check the length of a list
def test_len():
    a = [1, 2, 3]
    assert len(a) == 3, "The length of the list should be 3"

# Check append() adds an element at the end
def test_append():
    a = [1, 2, 3, 4, 5]
    a.append(6)
    assert a[-1]==6

# Check pop() removes the last element
def test_pop():
    a = [1, 2, 3, 4, 5]
    removed = a.pop()
    with pytest.raises(AssertionError):
        assert removed == 4

# Check if all elements in a list are integers
def is_list_of(obj, elem_type):
    # return isinstance(obj, list) and len(obj) > 0
    if not isinstance(obj, list):
        return False
    return all(isinstance(x,elem_type) for x in obj)

def test_list_integers():
    assert is_list_of([1,2,3], int) == True