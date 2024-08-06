class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sum = 0
        ans = 0
        for i in nums:
            if i == 0:
                sum = 0
            sum += i
            ans = max(ans, sum)
        return ans    

        
