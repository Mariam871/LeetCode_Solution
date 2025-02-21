from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # Hash set for quick lookup
        self.recover(root, 0)  # Start recovery with root value = 0

    def recover(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val
        self.values.add(val)  # Store in hash set
        
        # Recursively recover left and right children
        self.recover(node.left, 2 * val + 1)
        self.recover(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values  # O(1) lookup
