#include <iostream>
using namespace std;
string s = "babad";

class Solution
{
public:
    string longestPalindrome(string s)
    {
        int i = 0, j = 0, n = s.size(), lmax = 0;
        string p;
        while (i < n)
        {
            int i1 = i, j1 = j;
            while (j1 >= 0 && i1 < n)
            {
                if (s[i1++] != s[j1--])
                    break;
                int l = i1 - j1 - 1;
                if (l > lmax)
                {
                    lmax = l;
                    p = s.substr(j1 + 1, l);
                }
            }
            if (i == j)
                i++;
            else
                j++;
        }
        cout << p;
        return p;
    }
};

int main()
{
    cout << "Hello World!";
    Solution mySolution;
    mySolution.longestPalindrome(s);
    return 0;
}
