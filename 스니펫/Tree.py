class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal_recursive(root):
    def traverse(node):
        if node:
            result.append(node.val)  # Pre-order: Root -> Left -> Right
            traverse(node.left)
            traverse(node.right)

    result = []
    traverse(root)
    return result


def inorder_traversal_recursive(root):
    def traverse(node):
        if node:
            traverse(node.left)  # In-order: Left -> Root -> Right
            result.append(node.val)
            traverse(node.right)

    result = []
    traverse(root)
    return result


def postorder_traversal_recursive(root):
    def traverse(node):
        if node:
            traverse(node.left)
            traverse(node.right)  # Post-order: Left -> Right -> Root
            result.append(node.val)

    result = []
    traverse(root)
    return result

# 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 재귀 방식 출력
print("Pre-order (Recursive):", preorder_traversal_recursive(root))  # [1, 2, 4, 5, 3, 6, 7]
print("In-order (Recursive):", inorder_traversal_recursive(root))    # [4, 2, 5, 1, 6, 3, 7]
print("Post-order (Recursive):", postorder_traversal_recursive(root))# [4, 5, 2, 6, 7, 3, 1]
