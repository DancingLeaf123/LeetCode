#include "leetcode_common.h"

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int n = nums.size();
        int left = 0, right = n - 1, ans = n;
        while (left <= right)
        {
            int mid = (right - left) / 2 + left;
            if (target <= nums[mid])
            {
                ans = mid;
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }
        return ans;
    }
};
