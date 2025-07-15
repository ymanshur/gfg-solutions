class Solution {
  public:
    int buyMaximumProducts(int n, int k, int price[]) {
        int total = 0;
        
        vector<pair<int, int>> pricei;
        for (int i = 0; i < n; i++) {
            pricei.push_back(make_pair(price[i], i + 1));
        }
        
        sort(pricei.begin(), pricei.end());
        
        // for (int i = 0; i < n; i++) {
        //     cout << iprice[i][0] << " ";
        // }
        // cout << endl;
        
        int pr, nbuy;
        for (int i = 0; i < n; i++) {
            pr = pricei[i].first;
            nbuy = min(pricei[i].second, k / pr);
            total += nbuy;
            k -= pr * nbuy;
        }
        //cout << endl;
        
        return total;
    }
};
