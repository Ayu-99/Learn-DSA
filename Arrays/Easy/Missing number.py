class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=len(nums)
        for i in range(len(nums)): #0,1,2,3
            ans^=nums[i]
            ans^=i

        return ans 
