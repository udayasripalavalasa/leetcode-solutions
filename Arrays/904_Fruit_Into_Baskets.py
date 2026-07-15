class Solution(object):
    def totalFruit(self, fruits):
        left=0
        right=0
        max_length=0
        baskets={}
        while(right<len(fruits)):
            if fruits[right] in baskets:
                baskets[fruits[right]]=baskets[fruits[right]]+1
            else:
                baskets[fruits[right]]=1
            if len(baskets)>2:
                baskets[fruits[left]]=baskets[fruits[left]]-1
                if(baskets[fruits[left]]==0):
                    del baskets[fruits[left]]
                left=left+1
            if len(baskets)<=2:
                max_length=max(max_length,right-left+1)
            right=right+1
        return max_length