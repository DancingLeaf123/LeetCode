#include "leetcode_common.h"

// 你的 LeetCode 代码可以从这里开始写


class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num_set;
        for (const auto& num : nums) {
            num_set.insert(num);
        }

        int longestStreak = 0;

        for (const auto& num : num_set) {
            if (!num_set.count(num - 1)) {
                auto currentNum = num;
                auto currentStreak = 1;

                while (num_set.count(currentNum + 1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }

                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;           
    }
};






// 示例 1：

// 输入：nums = [100,4,200,1,3,2]
// 输出：4
// 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

// 示例 2：
// 输入：nums = [0,3,7,2,5,8,4,6,0,1]
// 输出：9