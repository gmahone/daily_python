class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
def length(node):
    if node is None:
        return 0
    length = 0
    while node.next is not None:
        length += 1
        node = node.next
    print(length)
    pass
  
def count(node, data):
    print(node)
    pass
