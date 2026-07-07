class Solution(object):
    def maxDepth(self, s):
        depth=0
        max_depth=0
        for ch in s:
            if(ch=="("):
                depth=depth+1
                max_depth=max(max_depth,depth)
            elif(ch==")"):
                depth=depth-1
        return max_depth
