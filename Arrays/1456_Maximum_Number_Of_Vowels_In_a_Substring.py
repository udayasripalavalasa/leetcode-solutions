class Solution(object):
    def maxVowels(self, s, k):
        count=0
        for i in range(k):
            if s[i] in 'aeiou':
                count=count+1
        max_count=count
        left=0
        right=k
        while right<len(s):
            if s[left] in 'aeiou':
                count=count-1
            left=left+1
            if s[right] in 'aeiou':
                count=count+1
            right=right+1
            max_count=max(max_count,count)
        return max_count