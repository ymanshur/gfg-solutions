// User function template for C++
class Solution {
  public:
    void pushZerosToEnd(vector<int>& arr) {
        int p = -1;
        for (int i = 0; i < arr.size(); i++)
        {
            if (p == -1 && arr[i] == 0)
            {
                p = i; // first zero in array
                continue;
            }
    
            if (p == -1)
                continue;
    
            if (arr[i] > 0)
            {
                swap(arr[p], arr[i]);
                p++;
            }
        }
    }
};
