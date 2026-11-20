# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = [root]
        rightView = []

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.right)
                    q.append(node.left)
            if level:
                rightView.append(level[0])
        
        return rightView