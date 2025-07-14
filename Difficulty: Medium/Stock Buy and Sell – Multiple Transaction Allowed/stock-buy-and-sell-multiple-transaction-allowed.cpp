
class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        // code here
        int total = 0;
        
        for (int i = 0; i < prices.size() - 1; i++) {
            int profit = prices[i + 1] - prices[i];
            
            if (profit > 0) {
                //cout << prices[i + 1] << " " << prices[i] << endl;
                total += profit;
            }
        }
        
        return total;
    }
};
