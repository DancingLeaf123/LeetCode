#include "leetcode_common.h"


// abcac
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0) return 0;
        unordered_set<char> temp_longest;
        int maxStr = 0;
        int left = 0;
        for(int i = 0; i < s.size(); i++){
            while (temp_longest.find(s[i]) != temp_longest.end()){
                temp_longest.erase(s[left]);
                left ++;
            }
            maxStr = max(maxStr,i-left+1);
            temp_longest.insert(s[i]);
    }
        return maxStr; 
    }
};



// 示例 1:

// 输入: s = "abcabcbb"
// 输出: 3 
// 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
// 示例 2:

// 输入: s = "bbbbb"
// 输出: 1
// 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
// 示例 3:

// 输入: s = "pwwkew"
// 输出: 3
// 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
//      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。