class Solution {
public:
    int maxProfit(vector<int>& prices) {
                int n = prices.size();
        int maxRight = 0;
        int maxProfit = 0;
        for(int i = n - 1; i >= 0; i--){
            maxRight = max(prices[i], maxRight);
            maxProfit = max(maxProfit, maxRight - prices[i]);
        }
        
        return maxProfit;
        
    }
};
