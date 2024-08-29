class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            x=nums[i]
            l=i+1
            r=len(nums)
         
            while l<r:
                if x + nums[l] + nums[r] == 0:
                    result.append([x,nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while r>l and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                     
                elif nums[l]+nums[r] + x < 0:
                    l+=1
                else:
                    r-=1
                
                
        return result         
                    
                    
                    
            
