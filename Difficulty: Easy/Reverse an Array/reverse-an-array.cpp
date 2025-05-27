class Solution {
  public:
    void reverseArray(vector<int> &arr) {
        for (int i = 0; i < arr.size() / 2; i++)
            swap(arr[i], arr[arr.size() - 1 - i]);
    }
};
