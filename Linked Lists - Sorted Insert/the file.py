""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""
def stringify(node):
    def helper(node2):
        return node2.data, node2.next
    if node is None:
        return 'None'
    string = ''
    data, node = helper(node)
    while not node is None:
        string += f'{data} -> '
        data, node = helper(node)
    string += f'{data} -> '
    string += 'None'
    return string

def parse(string):
    if string == 'None':
        return None
    values = string.split(' -> ')
    head = Node(int(values[0]))
    current = head
    for node in values[1:-1]:
        current.next = Node(int(node))
        current = current.next
    return head

def sorted_insert(head, data):
    list = stringify(head)
    if list == 'None':
        return Node(data)
    list = list.split(' -> ')[:1]
    for i, el in enumerate(list):
        if data > int(el):
            list = list[:i] + [str(data)] + list[i:]
            break
        continue
    list = ' -> '.join(list)
    list = parse(list)
    return list
