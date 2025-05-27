class Solution {
  public:

    // Function to rotate an array by d elements in counter-clockwise direction.
    void rotateArr(vector<int>& arr, int d) {
        int n = arr.size();
        int ncycle = gcd(n, d);
        for (int i = 0; i < ncycle; i++)
        {
            int toIdx = i;
            int startVal = arr[toIdx], fromIdx;
            while (true)
            {
                fromIdx = (toIdx + d) % n;
                if (fromIdx == i)
                    break;
                arr[toIdx] = arr[fromIdx];
                toIdx = fromIdx;
            }
            arr[toIdx] = startVal;
        }
    }

  private:
  
    // Function to return GCD of provided parameneter
    int gcd(int a, int b)
    {
        if (a < b)
            swap(a, b);
        
        int r = a % b;
        while (r > 0)
        {
            a = b;
            b = r;
            r = a % b;
        }
        
        return b;
    }
};