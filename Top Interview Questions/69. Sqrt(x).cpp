#include <limits.h>
#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return x;
        int left = 1, right = x/2;
        int mid = (left + right + 1) / 2;
        
        while (true)
        {
            if (mid == (x/mid))
            {
                return mid;
            }
            if (mid < (x/mid))
            {
                left = mid;
                if (mid+1 > x/(mid+1)) return mid;
                mid = (mid + right + 1) / 2;
            }
            if (mid > (x/mid))
            {
                right = mid;
                mid = (mid + left + 1) / 2;
                cout << mid << endl;
            }
        }
    }
};

int main(){
    Solution mysol;
    cout << "wtf" << endl;
    cout << mysol.mySqrt(1024);
    return 0;
}

