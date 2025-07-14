class Solution {
  public:
    int maxProfit(vector<int> &prices) {
        int total = 0; // total profit
        
        int n = prices.size();
        vector<int> profit(n, 0);
        int buy, sell = prices[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            buy = prices[i];
            if (buy > sell) {
                sell = buy;
            }
            
            profit[i] = max(profit[i + 1], sell - buy);
        }
        
        // for (int i = 0; i < n; i++) {
        //     cout << profit[i] << " ";
        // }
        // cout << endl;
        
        
        buy = prices[0];
        for (int i = 1; i < n; i++) {
            sell = prices[i];
            if (sell < buy) {
                buy = sell;
                continue;
            }
            
            //cout << sell << " " << buy << endl;
            
            // total = max(total, (sell - buy) + maxSubProfit(prices, i+1)); // 2 transactions
            total = max(total, (sell - buy) + profit[i]); // 1 transaction + 1 postfix transaction
        }
        
        return total;
    }
    
    int maxSubProfit(vector<int> &prices, int start) {
        int total = 0; // total sub profit
        int n = prices.size();
        int buy = prices[start];
        int sell;
        
        for (int i = start + 1; i < n; i++) {
            sell = prices[i];
            if (sell < buy) {
                buy = sell;
                continue;
            }
            
            total = max(total, sell - buy); // 1 transaction
        }
        
        return total;
    }
};