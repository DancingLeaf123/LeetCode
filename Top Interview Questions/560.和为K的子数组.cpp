#include "LT.h"

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int cur_max = nums[0];
        int cur_sum = 0;
        int left = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            cur_sum += nums[i];
            cur_max = max(cur_max, cur_sum);
            if (nums[i] < 0)
            {
                left++;
                cur_sum -= nums[i];
            }
        }
    }
};