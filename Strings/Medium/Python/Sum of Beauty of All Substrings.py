class Solution:
    def get_min_count(self, freq):
        min_count = float('inf')
        for count in freq:
            if count != 0:
                min_count = min(min_count, count)
        return min_count
    
    def get_max_count(self, freq):
        max_count = 0
        for count in freq:
            max_count = max(max_count, count)
        return max_count
    
    def beauty_sum(self, s):
        sum_beauty = 0
        n = len(s)
        for i in range(n):
            freq = [0] * 26  # Initialize frequency array to 0
            for j in range(i, n):
                freq[ord(s[j]) - ord('a')] += 1
                beauty = self.get_max_count(freq) - self.get_min_count(freq)
                sum_beauty += beauty
        return sum_beauty
