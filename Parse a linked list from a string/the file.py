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

def linked_list_from_string(s):
    return parse(s)
