from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    node = Node(data)
    node.next = head
    return node

def build_one_two_three():
    linked_list = Node(3)
    linked_list = push(linked_list, 2)
    linked_list = push(linked_list, 1)
    return linked_list
