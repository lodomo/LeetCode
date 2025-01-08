class Solution {
  public:
    int countPrefixSuffixPairs(vector<string> &words) {
        int n = words.size();
        int ans = 0;

        for (int i = 0; i < n; i++) {
            int xfix_len = words[i].size(); 
            for (int j = i + 1; j < n; j++) {
                int word_len = words[j].size();

                if (xfix_len > word_len) {
                    continue;
                }

                for (int k = 0, l = word_len - xfix_len; k < xfix_len; k++, l++) {
                    if (words[j][k] != words[i][k] || words[j][l] != words[i][k]) {
                        break;
                    }

                    if (k == xfix_len - 1) {
                        ans++;
                    }
                }
            }
        }

        return ans;
    }
};
