public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> res = new ArrayList<Integer>();
        
        if (matrix.length == 0) {
            return res;
        }
        
        int top = 0;
        int bottom = matrix.length-1;
        int left = 0;
        int right = matrix[0].length - 1;
        
        while (top <= bottom && left <= right) {
            // Traverse Right
            for (int j = left; j <= right; j ++) {
                res.add(matrix[top][j]);
            }
            top++;
            
            // Traverse Down
            for (int j = top; j <= bottom; j ++) {
                res.add(matrix[j][right]);
            }
            right--;
            
            if (top <= bottom) {
                // Traverse Left
                for (int j = right; j >= left; j --) {
                    res.add(matrix[bottom][j]);
                }
            }
            bottom--;
            
            if (left <= right) {
                // Traver Up
                for (int j = bottom; j >= top; j --) {
                    res.add(matrix[j][left]);
                }
            }
            left++;
        }
        
        return q;
    }
}
