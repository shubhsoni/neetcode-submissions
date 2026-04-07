# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        '''
        HINT: start with a complete example to not confuse yourself

        HINT: use complete tree for clear picture
        
              4
          2       6
        1   3   5   7

                    r
        preorder = [4,2,1,3,6,5,7] #<- 1st is always root
        inorder  = [1,2,3,4,5,6,7] #<- location of root defines the boundary of left and right-> mid
                          m
         '''    

        if not preorder or not inorder:
            return None

        index = {val:i for i,val in enumerate(inorder)}

        root = TreeNode(val = preorder[0])
        mid  = index[preorder[0]] #<---  O(1) lookup

        root.left  = self.buildTree(preorder[      1 : mid + 1], inorder[        : mid ])
        root.right = self.buildTree(preorder[mid + 1 :        ], inorder[mid + 1 :     ])
        return root 



        