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
