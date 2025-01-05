/*
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_last = {}
        result = 0

        for i, c in enumerate(s):
            if c not in first_last:
                first_last[c] = [i, 0]
            first_last[c][1] = i

        for c in first_last:
            left, right = first_last[c]
            result += len(set(s[left+1:right]))

        return result
*/

#include <string>
#include <unordered_map>
#include <utility>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, pair<int, int>> first_last;
        int result = 0;

        for (int i = 0; i < s.size(); i++) {
            if (first_last.find(s[i]) == first_last.end()) {
                first_last[s[i]] = {i, 0};
            }
            first_last[s[i]].second = i;
        }

        for (auto& [c, lr] : first_last) {
            int left = lr.first;
            int right = lr.second;
            std::unordered_map<char, int> seen;
            for (int i = left + 1; i < right; i++) {
                seen[s[i]] = 1;
            }
            result += seen.size();
        }

        return result;
    }
};
