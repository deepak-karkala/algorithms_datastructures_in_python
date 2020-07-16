"""Stack
"""


# Author: Deepak Karkala

class Stack:
    """
    Stack class
    """

    def __init__(self):
        self.stack = []

    @property
    def size(self):
        """Returns size of stack
        Returns
        --------
        Size of stack
        """
        return len(self.stack)

    @property
    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        """Returns top element of stack
        Returns
        -------
        Top element of stock

        Raises
        ------
        Exception
            if Stack is empty
        """
        if self.is_empty:
            raise IndexError("Stack empty")
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def show(self):
        return self.stack


if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(5)
    s.push(1)
    print(s.show())
    print(s.is_empty)
    print(s.size)
    s.pop()
    print(s.show())
    s.peek()
    print(s.show())
    s.push(10)
    print(s.show())
