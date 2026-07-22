class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        s=set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while(left<right):
                if(nums[i]+nums[left]+nums[right]==0):
                    s.add((nums[i],nums[left],nums[right]))
                    left=left+1
                    right=right-1
                elif(nums[i]+nums[left]+nums[right]>0):
                    right=right-1
                else:
                    left=left+1
        return [list(x) for x in s]