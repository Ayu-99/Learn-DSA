class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        l=[]
        for i in range(numRows):
            x=[0]*(i+1)
            l.append(x)
        for i in range(numRows):
        
            l[i][0]=1
            l[i][len(l[i])-1]=1
            
            for j in range(1,len(l[i])-1):
                    
                l[i][j]=l[i-1][j-1]+l[i-1][j]
            
        return l 
