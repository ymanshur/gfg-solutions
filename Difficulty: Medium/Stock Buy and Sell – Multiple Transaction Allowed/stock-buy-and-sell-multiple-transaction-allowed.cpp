
class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        int total = 0;
        
        // for (int i = 0; i < prices.size() - 1; i++) {
        //     int profit = prices[i + 1] - prices[i];
            
        //     if (profit > 0) {
        //         //cout << prices[i + 1] << " " << prices[i] << endl;
        //         total += profit;
        //     }
        // }
        
        int buy; // min price (local buy)
        int sell; // max price (local sell) 
        int n = prices.size();
        
        for (int i = 0; i < n - 1;) {
            while (i < n - 1 && prices[i] > prices[i + 1]) { i++; }
            buy = prices[i];
            while (i < n - 1 && prices[i] <= prices[i + 1]) { i++; }
            sell = prices[i];
            
            //cout << buy << " " << sell << endl;
            total += sell - buy;
        }
        
        return total;
    }
};
