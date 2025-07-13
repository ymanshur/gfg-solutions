class Solution {
  public:
    int maximumProfit(vector<int> &prices) {
        // The task is to compare profit for each combination of transaction and return max profit;
        // The simplest way to do the task is to evalute each combination through nested looping (brute-force);
        // It will takes approximately n^2 operations without any extra space;
        // The calculation is (n-1) + (n-2) + .. + 1 = n * (n-1) / 2
        //                                          ~= n^2
        // So brute-force will takes O(n^2) and O(1).
        
        /*
        int ans = 0; // max profit
        
        for (int i = 0; i < prices.size() - 1; i++)
        {
            for (int j = i + 1; j < prices.size(); j++)
            {
                int profit = prices[j] - prices[i];

                if (profit > ans)
                {
                    ans = profit;
                }
            }
        }
        
        return ans;
        */
        
        // Seems we got 'Time limit exceeded' of 1110/1115 test cases
        // So consider to refine the approach so it just takes O(n) of complexity.
        // To avoid nested loop, we can use Two-Pointer approach
        // Let buy and sell and we need to keep sell > buy as max profit cancidate
        // Loop through prices for the sell value and extend the buy value once sell < buy
        
        if (prices.size() == 1)
        {
            return 0;
        }
        
        int ans = 0; // max profit
        int buy = 0;

        for (int sell = 1; sell < prices.size(); sell++)
        {
            int profit = prices[sell] - prices[buy];
            
            if (profit < 0)
            {
                buy = sell;
                continue;
            }
            
            if (profit > ans)
            {
                ans = profit;
            }
        }
        
        return ans;
    }
};
