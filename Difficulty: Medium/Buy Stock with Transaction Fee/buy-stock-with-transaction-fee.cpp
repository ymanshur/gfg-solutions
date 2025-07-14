class Solution {
  public:
    int maxProfit(vector<int>& arr, int k) {
        int profit = 0;
        
        int n = arr.size();
        
        int buy, sell = 0;
        for (int i = n - 1; i >= 0; i--) {
            int notBuy;
            
            buy = max(profit, sell - arr[i] - k);
            notBuy = max(sell, arr[i] + profit);
            
            profit = buy;
            sell = notBuy;
        }
        
        return profit;
    }
};