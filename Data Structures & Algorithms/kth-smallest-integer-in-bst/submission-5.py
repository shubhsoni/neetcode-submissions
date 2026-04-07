# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # practice inorder, preorder, postorder

        if not root:
            return None
        
        ans = []
        def traverse(node, order='inorder'):
            if not node:
                return 

            if order=='inorder':
                traverse(node.left)
                ans.append(node.val)
                traverse(node.right)

            if order=='preorder':
                ans.append(node.val)
                traverse(node.left)
                traverse(node.right)

            if order=='postorder':
                traverse(node.right)
                ans.append(node.val)
                traverse(node.left)
                

        traverse(root)
        print('inorder')
        print(ans)

        # ans = []
        # traverse(root, 'preorder')
        # print('preorder')
        # print(ans)


        # ans = []
        # traverse(root, 'postorder')
        # print('postorder')
        # print(ans)

        return ans[k-1]
        