#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty()) return "";
        for (size_t i=0; i<strs.front().size(); ++i) {
            for (const auto &str : strs){
                if (i == str.size() || str.at(i) != strs.front().at(i)){
                    return strs.front().substr(0, i); 
                }
            }
        }
        return strs.front();
    }
};


int main() {
  string greeting = "Hello\n";
  cout << greeting << endl;
  vector<string> strs = {"flower","flow","flight"};
  Solution mys;
  cout << mys.longestCommonPrefix(strs);
  return 0;
}