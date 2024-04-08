class Node(object):
    def __init__(self, data):
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

def remove_duplicates(head):
    list_str = stringify(head)
    list_str = list_str.split(' -> ')[:-1]
    list_str_set = set(list_str)
    new_list = []
    for el in list_str:
        if el in list_str_set:
            new_list.append(el)
            list_str_set.remove(el)
    new_list.append('None')
    new_list = ' -> '.join(new_list)
    return parse(new_list)
