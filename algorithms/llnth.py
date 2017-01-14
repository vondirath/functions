class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    list_item = ll
    from_end = ll

    if m < 0 or m == None:
        return
    elif m == 0:
        m = 1
    else:
        m = (m + 1)

    for index in xrange(m):
        list_item = list_item.next
    while list_item is not None:
        list_item = list_item.next
        from_end = from_end.next
    return from_end.data


ll = Node(0)
ll.next = Node(1)
ll.next.next = Node(2)
ll.next.next.next = Node(3)
ll.next.next.next.next = Node(4)
ll.next.next.next.next.next = Node(5)



print question5(ll, 2)
print question5(ll, 3)
print question5(ll, 0)
