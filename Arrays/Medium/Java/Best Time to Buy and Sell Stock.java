class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int maxRight = 0;
        int n = prices.length; 
        for(int i=n-1; i>=0; i--) {
            maxRight = Math.max(maxRight, prices[i]);
            maxProfit = Math.max(maxProfit, maxRight-prices[i]);
        }
        return maxProfit;
    }
}
