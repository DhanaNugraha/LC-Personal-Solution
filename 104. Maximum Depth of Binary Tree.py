# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive DFS solution
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # if root reaches the end, return 0
        if not root:
            return 0
        
        # Try traversing in image given to understand
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# BFS solution (First In First Out)
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # if root empty return -
        if not root:
            return 0
        
        level = 0
        queue = collections.deque([root])

        # loop for all stage
        while queue:
            # loof for current stage
            for i in range(len(queue)):
                currentNode = queue.popleft()

                # if next node exist, put in queue
                if currentNode.left:
                    queue.append(currentNode.left)
                
                if currentNode.right:
                    queue.append(currentNode.right)

            # done for this level loop
            level += 1

        return level
    

# Iterative DFS solution (Last In First Out)
import collections
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # if root empty return -
        if not root:
            return 0
        
        # [current node, depth]
        queue = [[root], 1]
        outputDepth = 1

        # loop while queue not empty
        while queue:
            # take the Last In node in queue list
            node, depth = queue.pop()

            # if node not None
            if node:
                # update max depth
                output = max(output, depth)
                # append right sub root
                queue.append([root.right, depth + 1])
                # Last In append left sub root
                queue.append([root.left, depth + 1])

        return outputDepth