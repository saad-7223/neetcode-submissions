# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        maxElement = []

        while q:
            qlen  = len(q)
            maxNode = float('-inf')
            for i in range(qlen):
                node = q.popleft()
                if node:
                    maxNode = max(maxNode,node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            maxElement.append(maxNode)

        return maxElement