class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # maintain an ans array with k elements

        # while traversing, append new item if its smaller than existing elements

        # how do we know if kth item is smaller than already saved k-1 items ?

        # data structure to store only k smallest elements? -> min-heap
        #    -> store items in min heap instead of array
        #.   -> after traversal the remaining element at top would be the ans

        if not root:
            return None

        ans = []

        stack = [root]
        while stack:
            node = stack.pop()
            
            heapq.heappush(ans, node.val)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        for _ in range(k - 1):
            heapq.heappop(ans)
            
        return heapq.heappop(ans)