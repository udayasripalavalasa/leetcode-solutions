class Solution(object):
    def maxSubArray(self, nums):
        m_sum=nums[0]
        s=0
        n=len(nums)
        for i in range(n):
            s=s+nums[i]
            if(s>m_sum):
                m_sum=s
            if(s<0):
                s=0

        return m_sum
        