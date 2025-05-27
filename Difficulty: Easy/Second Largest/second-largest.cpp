// User function template for C++
class Solution {
  public:
    // Function returns the second
    // largest elements
    int getSecondLargest(vector<int> &arr) {
        if (arr.size() == 0)
        return -1;

        int max = arr[0], res = -1;
        for (int i = 1; i < arr.size(); i++)
        {
            if (arr[i] > max)
            {
                res = max;
                max = arr[i];
            }
            else if (arr[i] < max && arr[i] > res)
                res = arr[i];
        }
        
        return res;
    }
};
