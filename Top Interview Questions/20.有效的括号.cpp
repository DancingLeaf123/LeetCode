#include "LT.h"

class Solution
{
public:
    bool isValid(string s)
    {
        unordered_map<char, char> m = {{'?', '?'},{'(', ')'}, {'{', '}'}, {'[', ']'}};
        stack<char> st;
        st.push('?');
        for (char c : s)
        {
            if (m.find(c) != m.end()) st.push(c);
            else{
                if(m[st.top()] != c) return false;
                else  st.pop();
            }
        }
        return st.size() == 1;
    }
};
