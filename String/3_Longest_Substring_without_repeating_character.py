class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        for i in range(len(s)):
            ans=""
            for j in range(i,len(s)):
                if s[j] in ans:
                    break
                ans=ans+s[j]
                l=max(l,len(ans))
        return l
        