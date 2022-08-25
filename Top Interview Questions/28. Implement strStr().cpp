#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.empty()) return 0;
        int n_s = needle.size();
        int h_s = haystack.size();
        for (size_t i = 0; i < h_s; i++)
        {
            if (haystack.substr(i,n_s) == needle) return i;
        }
        return -1;
    }
};