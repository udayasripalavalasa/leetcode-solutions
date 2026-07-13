class Solution(object):
    def sequentialDigits(self, low, high):
        l=[1,2,3,4,5,6,7,8,9]
        re=[]
        for i in range(len(l)):
            ans=""
            for j in range(i,len(l)):
                ans=ans+str(l[j])
                if(low<=int(ans)<=high):
                    re.append(int(ans))
        return sorted(re)
        