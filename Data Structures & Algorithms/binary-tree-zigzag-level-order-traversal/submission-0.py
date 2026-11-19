# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        levelCounter = 1
        q = [root]
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.pop(0)
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level : 
                if levelCounter % 2 != 0:
                    result.append(level)
                else:
                    result.append(level[ : :-1])
            levelCounter += 1
        return result 