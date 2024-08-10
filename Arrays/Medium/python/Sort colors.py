class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # code here
        n = len(arr)
        l, m, h = 0, 0, n-1
        
        while m <= h:
            if arr[m] == 0:
                arr[m],arr[l] = arr[l], arr[m]
                l += 1
                m += 1
            
            elif arr[m] == 1:
                m += 1
            
            else:
                arr[m], arr[h] = arr[h], arr[m]
                h -= 1
        
