# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isMirror(self,t1:TreeNode,t2:TreeNode):
        if(t1 is None and t2 is None):
            return True
        if(t1 is None or t2 is None):
            return False
        return (t1.val==t2.val) and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        if(root.left is None and  root.right is None):
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right)+1
    
    def hasSum(self,root:TreeNode,sum,cur):
        if(root is None):
            return False
        cur+=root.val
        if(cur==sum and root.left is None and root.right is None):
            return True
        return (self.hasSum(root.right,sum,cur) or self.hasSum(root.left,sum,cur))

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasSum(root,sum, 0)
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None):
            return None
        if(root.val==p.val or root.val==q.val):
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if(left is None):
            return right
        elif(right is None):
            return left
        else:
            return root
        
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.res = None
        self.helper(root) # this is nothing but inoreder in bst inorder gives sorted vale of the data
        return self.res

    def helper(self, root):
        if not root:
            return
        self.helper(root.left)
        
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.helper(root.right)
        
        
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if(root is None):
            return "X#"

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        return str(root.val)+"#"+leftSerialized+rightSerialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            val = next(data)
            if val == 'X':
                return None
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        data = iter(data.split("#"))
        return dfs()
    
    
    
    ans = -float("inf")
    def solution(self,node):
        if(node is None):
            return 0
        left = self.solution(node.left)
        right = self.solution(node.right)

        mxSide = max(node.val,max(left,right)+node.val)
        mxTop = max(mxSide,left+right+node.val)
        self.ans = max(self.ans,mxTop)
        return mxSide

    def maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        return self.ans