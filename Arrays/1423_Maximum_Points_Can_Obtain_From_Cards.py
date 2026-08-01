class Solution(object):
    def maxScore(self, cardPoints, k):
        left_sum=0
        right_sum=0
        max_sum=0
        for i in range(k):
            left_sum=left_sum+cardPoints[i]
        max_sum=left_sum
        j=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            left_sum=left_sum-cardPoints[i]
            right_sum=right_sum+cardPoints[j]
            j=j-1
            max_sum=max(max_sum,left_sum+right_sum)
        return max_sum