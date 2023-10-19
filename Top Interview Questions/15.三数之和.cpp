#include "leetcode_common.h"

class Solution
{
public:
    vector<vector<int>> threeSum(vector<int> &nums)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end()); // 首先对输入数组排序
        vector<vector<int>> ans;        // 用于存储结果的二维向量

        if (nums.front() > 0 || nums.back() < 0)
        {
            return ans; // 如果数组中的元素全部为正数或全部为负数，直接返回空结果
        }

        if (nums.front() == 0 && nums.back() == 0)
        {
            ans.push_back({0, 0, 0}); // 如果数组中的元素全部为0，返回[0, 0, 0]作为结果
            return ans;
        }

        // 枚举 a
        for (int first = 0; first < n; ++first)
        {
            // 需要和上一次枚举的数不相同
            if (first > 0 && nums[first] == nums[first - 1])
            {
                continue;
            }

            // c 对应的指针初始指向数组的最右端
            int third = n - 1;
            // int target = -nums[first]; 

            // 枚举 b
            for (int second = first + 1; second < n; ++second)
            {
                // 需要和上一次枚举的数不相同
                if (second > first + 1 && nums[second] == nums[second - 1])
                {
                    continue;
                }

                // 需要保证 b 的指针在 c 的指针的左侧
                while (second < third && nums[first] + nums[second] + nums[third] > 0)
                {
                    --third;
                }

                // 如果指针重合，随着 b 后续的增加
                // 就不会有满足 a + b + c = 0 并且 b < c 的 c 了，可以退出循环
                if (second == third)
                {
                    break;
                }

                if (nums[first] + nums[second] + nums[third] ==  0)
                {
                    ans.push_back({nums[first], nums[second], nums[third]});
                }
            }
        }
        return ans; // 返回结果
    }
};