# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = defaultdict(list)

        q = [(root,0)]
        
        while q:
            node , nodePos = q.pop(0)
            result[nodePos].append(node.val)

            if node.left:
                q.append(
                    (node.left , nodePos+1)
                )
            
            if node.right:
                q.append(
                    (node.right , nodePos +1)
                )
            
        
        order = [item for item in result.values()]


        return order
