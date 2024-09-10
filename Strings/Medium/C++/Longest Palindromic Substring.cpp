class Solution {
public:
    std::string longestPalindrome(const std::string& S) {
        int start = 0;
        int maxLen = 1;

        int n = S.length();
        for (int i = 1; i < n; ++i) {
            // Even length palindrome
            int l = i - 1;
            int r = i;
            while (l >= 0 && r < n && S[l] == S[r]) {
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    start = l;
                }
                --l;
                ++r;
            }

            // Odd length palindrome
            l = i - 1;
            r = i + 1;
            while (l >= 0 && r < n && S[l] == S[r]) {
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    start = l;
                }
                --l;
                ++r;
            }
        }

        return S.substr(start, maxLen);
    }
};
