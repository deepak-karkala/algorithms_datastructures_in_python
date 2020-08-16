"""
Singly linked list
"""


class Node:
    """
    Individual nodes in linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class SinglyLinkedList:
    """
    Singly linked list class
    """

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        Iterator to traverse a linked list
        :return: individual node
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        """
        Add node to beginning of list
        :param node: Node object
        :return:
        """
        node.next = self.head
        self.head = node

    def add_last(self, node):
        """
        Add node at the end
        :param node: Node object
        :return:
        """
        if not self.head:
            self.head = node
            return
        n = self.head
        for current_node in self:
            pass
        current_node.next = node


if __name__ == "__main__":
    sllist = SinglyLinkedList(["a", "b", "c", "d", "e"])
    print(sllist)
    for n in sllist:
        print(n)
    sllist.add_first(Node("z"))
    print(sllist)
    sllist.add_last(Node("f"))
    print(sllist)
