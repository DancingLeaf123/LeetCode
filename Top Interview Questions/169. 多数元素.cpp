#include "leetcode_common.h"

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;
        int majority=0, majority_count=0;
        for(int num : nums) {
            counts[num]++;
            if(majority_count < counts[num]) {
                majority = num;
                majority_count = counts[num];
            }
        }
        return majority;
    }
};

