class BSTNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def question4(root, n1, n2):
    if root.value > n1 and root.value > n2:
        return question4(root.left, n1, n2)
    if root.value < n1 and root.value < n2:
        return question4(root.right, n1, n2)
    return root.value

root = BSTNode(20)
root.left = BSTNode(8)
root.right = BSTNode(22)
root.left.left = BSTNode(4)
root.left.right = BSTNode(12)
root.left.right.left = BSTNode(10)
root.left.right.right = BSTNode(14)

print question4(root, 10, 14)
print question4(root, 14, 8)
print question4(root, 10, 22)