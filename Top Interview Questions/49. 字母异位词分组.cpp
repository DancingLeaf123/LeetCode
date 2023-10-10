#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> up;
        for (string& str: strs) {
            string key = str;
            sort(key.begin(), key.end());
            up[key].emplace_back(str);
        }
        vector<vector<string>> ans;
        for (auto i = up.begin(); i != up.end(); ++i) {
            ans.emplace_back(i->second);
        }
        return ans;
    }
};

void printResult(const vector<vector<string>>& result) {
    cout << "[" << endl;
    for (const vector<string>& group : result) {
        cout << "  [";
        for (const string& str : group) {
            cout << "\"" << str << "\", ";
        }
        cout << "]," << endl;
    }
    cout << "]" << endl;
}

void runCustomTestCases() {
    Solution sol;

    // 示例测试用例
    vector<string> test1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> result1 = sol.groupAnagrams(test1);
    
    // 打印结果
    cout << "case 1:" << endl;
    printResult(result1);

}


int main() {
    runCustomTestCases();
    return 0;
}
