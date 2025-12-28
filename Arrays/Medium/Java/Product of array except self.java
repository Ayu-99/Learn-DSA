//brute
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        int[] prefix = new int[n];
        int[] suffix = new int[n];
        int[] ans = new int[n];

        // Build prefix product array
        prefix[0] = 1;
        for(int i = 1; i < n; i++){
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        // Build suffix product array
        suffix[n - 1] = 1;
        for(int i = n - 2; i >= 0; i--){
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        // Multiply prefix and suffix
        for(int i = 0; i < n; i++){
            ans[i] = prefix[i] * suffix[i];
        }

        return ans;
    }
}

//optimized
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];

        // prefix products
        ans[0] = 1;
        for(int i = 1; i < n; i++){
            ans[i] = ans[i - 1] * nums[i - 1];
        }

        // suffix running product
        int suffix = 1;
        for(int i = n - 1; i >= 0; i--){
            ans[i] = ans[i] * suffix;
            suffix *= nums[i];
        }

        return ans;
    }
}
