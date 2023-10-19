#include "leetcode_common.h"

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        int n = height.size();
        int era = min(height[0],height[n - 1]) * (n-1);
        for (int i = 0, j = n - 1; i < j;)
        {
            if (height[i] < height[j])
            {
                ++i;
                era = max(era, min(height[i],height[j]) * (j-i));
            }
            else
            {
                --j;
                era = max(era, min(height[i],height[j]) * (j-i));
            }
        }
        return era;
    }
};