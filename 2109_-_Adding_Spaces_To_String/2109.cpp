#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    string addSpaces(string s, vector<int> &spaces) {
        int resultIndex = 0;
        int spacesIndex = 0;
        const int spacesSize = spaces.size();
        string result(s.size() + spaces.size(), ' ');

        for (int stringIndex = 0; stringIndex < s.size(); stringIndex++) {
            if (spacesIndex < spacesSize &&
                spaces[spacesIndex] == stringIndex) {
                ++spacesIndex;
                ++resultIndex;
            }
            result[resultIndex] = s[stringIndex];
            resultIndex++;
        }

    return result;
    }
};
