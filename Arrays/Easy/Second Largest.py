class Solution:sq
    def print2largest(self, arr):
        # Code Here
        first=-1
        second=-1
        
        for i in range(0, len(arr)):
            if arr[i] > first:
                second=first
                first=arr[i]
            elif arr[i] > second and arr[i] != first:
                second=arr[i]
        
        return sq 
