#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int strlen = s.size();
        vector<int> shift_list(strlen + 1, 0);
        const int FORWARD = 1;
        int delta = 0;

        for (auto& shift : shifts) {
            delta = shift[2] == FORWARD ? 1 : -1;
            shift_list[shift[0]] += delta;
            shift_list[shift[1] + 1] -= delta;
        }

        for (int i = 1; i < strlen; i++) {
            shift_list[i] += shift_list[i - 1];
        }

        for (int i = 0; i < strlen; i++) {
            int shift = (shift_list[i] + 26) % 26;
            s[i] = (s[i] - 'a' + shift) % 26 + 'a';
        }

        return s;
    }
};


