class Solution {
public:
int getMinCount(const std::vector<int>& freq) {
        int minCount = INT_MAX;
        for (int count : freq) {
            if (count != 0) {
                minCount = std::min(minCount, count);
            }
        }
        return minCount;
    }

    int getMaxCount(const std::vector<int>& freq) {
        int maxCount = 0;
        for (int count : freq) {
            maxCount = std::max(maxCount, count);
        }
        return maxCount;
    }
    int beautySum(string s) {
        int sum = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            std::vector<int> freq(26, 0); // Initialize frequency array to 0
            for (int j = i; j < n; ++j) {
                freq[s[j] - 'a']++;
                int beauty = getMaxCount(freq) - getMinCount(freq);
                sum += beauty;
            }
        }
        return sum;
    }
};
