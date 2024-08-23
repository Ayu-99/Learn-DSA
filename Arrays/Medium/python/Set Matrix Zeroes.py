class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(arr), len(arr[0])
        C0 = 1 #flag to know that whether first column should be marked 0 or not

        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    # mark i-th row:
                    arr[i][0] = 0 #row

                    # mark j-th column:
                    if j == 0:
                        C0 = 0
                    else:
                        arr[0][j] = 0

        # Mark with 0 from (1,1)
        # to (n-1, m-1):
        for i in range(1, n):
            for j in range(1, m):
                if arr[i][j] != 0:
                    # Check for col & row:
                    if arr[i][0] == 0 or arr[0][j] == 0:
                        arr[i][j] = 0

        # 1st row then 1st col:
        if arr[0][0] == 0:
            for j in range(m):
                arr[0][j] = 0
        if C0 == 0:
            for i in range(n):
                arr[i][0] = 0

            
