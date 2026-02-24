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

        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                cur_node = q.popleft()
                if cur_node:
                    level.append(cur_node.val)
                    q.append(cur_node.left)
                    q.append(cur_node.right)
            if level:
                res.append(level)

        return res                