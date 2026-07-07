class Solution(object):
    def removeOuterParentheses(self, s):
        co=0
        ans=""
        for ch in s:
            if(ch==")"):
                co=co-1
            if(co!=0):
                ans=ans+ch
            if(ch=="("):
                co=co+1
        return ans