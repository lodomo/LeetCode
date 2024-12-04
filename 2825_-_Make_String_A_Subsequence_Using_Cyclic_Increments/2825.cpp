class Solution {
  public:
    bool canMakeSubsequence(string str1, string str2) {
        int str1_len = str1.size();
        int str2_len = str2.size();
        if (str2_len > str1_len)
            return false;

        for (int i = 0, j = 0; i < str1_len; i++) {
            if (str1[i] == str2[j] || str1[i] + 1 == str2[j] ||
                (str1[i] == 'z' && str2[j] == 'a')) {
                ++j;
                if (j == str2_len) {
                    return true;
                }
            }
        }
        return false;
    }
};
