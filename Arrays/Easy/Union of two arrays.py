def findUnion(self,arr1,arr2,m,n):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i, j = 0, 0
        output=[]
        while i < m and j < n:
            while i+1<m and arr1[i+1]==arr1[i]:
                i+=1
                
            while j+1<n and arr2[j+1]==arr2[j]:
                j+=1
                
            if arr1[i] < arr2[j]:
                output.append(arr1[i])
                i += 1
            elif arr2[j] < arr1[i]:
                output.append(arr2[j])
                j+= 1
            else:
                output.append(arr1[i])
                j += 1
                i += 1
    
        # Print remaining elements of the larger array
        while i < m:
            while i+1<m and arr1[i+1]==arr1[i]:
                i+=1
            output.append(arr1[i])
            i += 1
    
        while j < n:
            while j+1<n and arr2[j+1]==arr2[j]:
                j+=1
            output.append(arr2[j])
            j += 1
        return output
