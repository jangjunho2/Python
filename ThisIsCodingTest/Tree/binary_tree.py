'''
preorder 전위 root left right
inorder 중위 left root right
postorder 후위  left right root
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


# preorder NLR # 전위순회
def recursivePreorder(node: TreeNode):
    if node is None:
        return
    print(node.val, end=" ")
    recursivePreorder(node.left)
    recursivePreorder(node.right)


print("\nrecursive Preorder : ", end="")
recursivePreorder(node1)

# inorder LNR # 중위순회


def recursiveInorder(node: TreeNode):
    if node is None:
        return
    recursiveInorder(node.left)
    print(node.val, end=" ")
    recursiveInorder(node.right)


print("\nrecursive Inorder : ", end="")
recursiveInorder(node1)


# postOrder LRN # 후위순회
def recursivePostorder(node: TreeNode):
    if node is None:
        return
    recursivePostorder(node.left)
    recursivePostorder(node.right)
    print(node.val, end=" ")


print("\nrecursive Postorder : ", end="")
recursivePostorder(node1)
