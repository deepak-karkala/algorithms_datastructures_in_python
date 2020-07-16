import pytest
from stack import Stack


class TestStack:
    """Unit tests for Stack class using pytest
    """
    def test_empty_stack_size(self):
        """Test empty stack size equals 0
        """
        s = Stack()
        assert s.size == 0

    def test_push(self):
        """Test pushing new element to top of stack
        """
        s = Stack()
        s.push(2)
        s.push(7)
        assert s.stack[-1] == 7

    def test_pop(self):
        """Test popping element from stack
        """
        s = Stack()
        s.push(2)
        s.push(7)
        assert s.pop() == 7

    def test_empty_stack_pop_exception(self):
        """Test popping from empty stack raises Exception
        """
        s = Stack()
        s.push(2)
        s.push(7)
        s.pop()
        s.pop()
        with pytest.raises(IndexError):
            s.pop()
