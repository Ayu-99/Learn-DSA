from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Create frequency counters for both strings
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        # Compare both counters
        return counter_s == counter_t
