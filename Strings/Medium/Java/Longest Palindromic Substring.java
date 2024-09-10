public class Solution {
    public String longestPalindrome(String S) {
        int start = 0;
        int maxLen = 1;
        int n = S.length();

        for (int i = 1; i < n; ++i) {
            // Even length palindrome
            int l = i - 1;
            int r = i;
            while (l >= 0 && r < n && S.charAt(l) == S.charAt(r)) {
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
            while (l >= 0 && r < n && S.charAt(l) == S.charAt(r)) {
                if (r - l + 1 > maxLen) {
                    maxLen = r - l + 1;
                    start = l;
           
