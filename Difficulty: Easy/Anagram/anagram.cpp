class Solution {
  public:
    // Function is to check whether two strings are anagram of each other or not.
    bool areAnagrams(string& s1, string& s2) {
        if (s1.size() != s2.size())
        {
            return false;
        }
        
        int alpha[26];
        for (int i = 0; i < 26; i++)
        {
            alpha[i] = 0;
        }
        
        for (int i = 0; i < s1.size(); i++)
        {
            int alphaIdx = s1[i] - 97;
            alpha[alphaIdx]++;
        }
        
        for (int i = 0; i < s2.size(); i++)
        {
            int alphaIdx = s2[i] - 97;
            if (alpha[alphaIdx] == 0)
            {
                return false;
            }
            
            alpha[alphaIdx]--;
        }
        
        return true;
    }
};