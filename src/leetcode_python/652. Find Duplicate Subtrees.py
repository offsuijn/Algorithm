# 652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/description/

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        ans = []
        
        def find(root):
            if not root: return ''
            
            encoded = str(root.val) + "#" + find(root.left) + "#" + find(root.right)
            
            seen[encoded] += 1
            if seen[encoded] == 2:
                ans.append(root)
            
            return encoded
    
        find(root)
        return ans
