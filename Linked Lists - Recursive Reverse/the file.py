class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

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

def reverse(head):
    list_str = stringify(head)
    list_str = list_str.split(' -> ')[:-1]
    list_str = list_str[::-1] + ['None']
    list_str = ' -> '.join(list_str)
    return parse(list_str)
