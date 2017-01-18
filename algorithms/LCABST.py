class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def question4(root, n1, n2):
    if root is None or root.value == n1 or root.value == n2:
        return root.value
    if root.value > n1 and root.value > n2:
        return question4(root.left, n1, n2)
    if root.value < n1 and root.value < n2:
        return question4(root.right, n1, n2)
    return root.value


root = Node(0)
root.right = Node(4)
root.right.left = Node(1)
root.right.right = Node(2)

print question4(root, 4, 2)
