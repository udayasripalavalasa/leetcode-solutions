class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        s=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while(left<right):
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if(sum==target):
                        s.add((nums[i],nums[j],nums[left],nums[right]))
                        left=left+1
                        right=right-1
                    elif(sum>target):
                        right=right-1
                    else:
                        left=left+1
        return [list(x) for x in s]


        