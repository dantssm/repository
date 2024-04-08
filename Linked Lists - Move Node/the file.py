class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    node = source.data
    source = source.next
    dest, dest.next = Node(node), dest
    return Context(source, dest)
