class Solution(object):
    def moveZeroes(self, nums):
        pos=0
        for i in nums:
            if(i!=0):
                nums[pos]=i
                pos=pos+1
        while pos<len(nums):
            nums[pos]=0
            pos=pos+1