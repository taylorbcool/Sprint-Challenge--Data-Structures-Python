class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # NON-RECURSIVE SOLUTION
        # now make this recursive...
        # def revList(sll):
        #     current = node
        #     prev = None
        #     while current is not None:
        #         next = current.next
        #         current.next = prev
        #         prev = current
        #         current = next
        #     return

        # base case, node will be none if the list has been reversed
        if node is None:
            return
        # set the current last/tail node in list to head of reversed list
        # can't just use tail because it's singly linked
        elif node.next_node is None:
            self.head = node
        # move back step by step and set next to prev, effectively flipping the links around
        # recursively setting next node to current node and current node to prev node
        # this works because of what the params are
        self.reverse_list(node.next_node, node)
        node.next_node = prev