from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root is None:
                return None
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

root = TreeNode(
    4,
    TreeNode(
        2,
        TreeNode(1),
        TreeNode(3)
    ),
    TreeNode(
        7,
        TreeNode(6),
        TreeNode(9)
    )
)

sol = Solution()
inverted_root = sol.invertTree(root)

def print_tree_pretty(node, level=0):
    if node is not None:
        print_tree_pretty(node.right, level + 1)
        print('    ' * level + f'-> {node.val}')
        print_tree_pretty(node.left, level + 1)

print_tree_pretty(inverted_root)
#
# from typing import Optional
#
#
# # 트리 노드 정의
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# # 트리 구조 보기 좋게 출력하는 함수
# def print_tree_pretty(node, level=0):
#     if node is not None:
#         print_tree_pretty(node.right, level + 1)
#         print('    ' * level + f'-> {node.val}')
#         print_tree_pretty(node.left, level + 1)
#
#
# # 트리를 뒤집는 함수 (디버깅 출력 포함)
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return None
#
#         # 디버깅 출력
#         print(f"Inverting node: {root.val}")
#
#         # 재귀적으로 왼쪽/오른쪽 뒤집기
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#
#         # 결과 디버깅 출력
#         print(
#             f"After invert node {root.val}: left={root.left.val if root.left else None}, right={root.right.val if root.right else None}")
#
#         return root
#
#
# # 샘플 트리 생성:     1
# #                   / \
# #                  2   3
# root = TreeNode(1, TreeNode(2), TreeNode(3))
#
# print("Before invert:")
# print_tree_pretty(root)
#
# # 트리 뒤집기
# sol = Solution()
# inverted_root = sol.invertTree(root)
#
# print("\nAfter invert:")
# print_tree_pretty(inverted_root)
