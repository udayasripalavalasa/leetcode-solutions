class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        right=0
        window_sum=0
        max_sum=0
        for right in range(k):
            window_sum=window_sum+nums[right]
        max_sum=window_sum
        right=k
        while(right<len(nums)):
            window_sum=window_sum-nums[left]
            left=left+1
            window_sum=window_sum+nums[right]
            right=right+1
            max_sum=max(max_sum,window_sum)
        return float(max_sum)/k
