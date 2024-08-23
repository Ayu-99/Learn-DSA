class Solution {
public:
    void setZeroes(vector<vector<int>>& arr) {
        int n = arr.size(), m = arr[0].size();

    int C0 = 1;

    // Traverse the arr and
    // mark 1st row & 1st
    // col as follows:
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 0) {

                // mark i-th row:
                arr[i][0] = 0;

                // mark j-th column:
                if (j == 0)
                    C0 = 0;
                else
                    arr[0][j] = 0;
            }
        }
    }

    // Mark with 0 from (1,1)
    // to (n-1, m-1):
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
            if (arr[i][j] != 0) {

                // Check for col & row:
                if (arr[i][0] == 0 || arr[0][j] == 0) {
                    arr[i][j] = 0;
                }
            }
        }
    }

    // Finally mark the
    // 1st row then 1st col:
    if (arr[0][0] == 0) {
        for (int j = 0; j < m; j++) {
            arr[0][j] = 0;
        }
    }
    if (C0 == 0) {
        for (int i = 0; i < n; i++) {
            arr[i][0] = 0;
        }
    }
    }
};
