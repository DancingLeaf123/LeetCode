#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        int e = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            if (digits[i] == 9) {
                digits[i] = 0;
                e = 1;
                if (i == 0) digits.insert(digits.begin(),1);
            }
            else{
                digits[i] = digits[i] + (e || 1);
                e = 0;
                break;
            }
        }
        return digits;
    }
};