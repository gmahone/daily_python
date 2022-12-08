class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
def length(node):
    if node is None:
        return 0
    length = 1
    while node.next is not None:
        node = node.next
        length += 1
    return length
  
def count(node, data):
    if node is None:
        return 0
    tmp_count = 0
    while True:
        if node.data == data:
            tmp_count += 1 
        if node.next is not None:
            node = node.next
        else:
            break
    return tmp_count
