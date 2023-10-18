#include "leetcode_common.h"

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int inf = 1e9;
        int minprice = inf, maxProfit = 0;
        for (int price:prices)
        {
            minprice = min(minprice, price);
            maxProfit = max(maxProfit, price - minprice);
        }
        return maxProfit;
    }
};