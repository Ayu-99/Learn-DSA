def largest_helper(self, n, arr, i):
        if i==n-1: #base element
            return arr[i]
        
        x = self.largest_helper(n, arr, i+1)
        return max(x, arr[i])
    
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        maxe = arr[0]
        for i in range(1, n):
            if arr[i] > maxe:
                maxe = arr[i]
        
        return maxe
