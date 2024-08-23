class Solution {
    public void setZeroes(int[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;

        int C0 = 1;

        // Traverse the matrix and mark 1st row & 1st col as
        // follows:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 0) {

                    // mark i-th row:
                    matrix[i][0] = 0;

                    // mark j-th column:
                    if (j == 0)
                        C0 = 0;
                    else
                        matrix[0][j] = 0;
                }
            }
        }

        // Mark with 0 from (1,1) to (n-1, m-1):
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (matrix[i][j] != 0) {

                    // Check for col & row:
                    if (matrix[i][0] == 0
                        || matrix[0][j] == 0) {
                        matrix[i][j] = 0;
                    }
                }
            }
        }

        // Finally mark the 1st row then 1st col:
        if (matrix[0][0] == 0) {
            Arrays.fill(matrix[0], 0);
        }
        if (C0 == 0) {
            for (int i = 0; i < n; i++) {
                matrix[i][0] = 0;
            }
        }

    }
}
