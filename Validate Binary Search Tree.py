# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        self.flag = True
        self.prev = None
        
        def isValid(root):
            if not root:
                return
            
            isValid(root.left)
            
            if self.prev and self.prev.val >= root.val:
                self.flag = False
                return
            self.prev = root
                
            isValid(root.right)

        isValid(root)
        return self.flag
