class Solution(object):
    def longestOnes(self, nums, k):
        left=0
        right=0
        le=0
        m_le=0
        zeros=0
        while right<len(nums):
            if(nums[right]==0):
                zeros=zeros+1
            if(zeros>k):
                if(nums[left]==0):
                    zeros=zeros-1
                left=left+1
            if(zeros<=k):
                le=right-left+1
                m_le=max(le,m_le)
            right=right+1
        return m_le

        