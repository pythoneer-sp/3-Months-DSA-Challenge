class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i=0
        j=0
        d=dict()
        for char in t:
            d[char] = d.get(char, 0) + 1
            
        count = len(d)
        min_len = float('inf') 
        start_index = 0    
        
        while j < len(s):
            if s[j] in d:
                d[s[j]] -= 1
                if d[s[j]] == 0:
                    count -= 1
            
            while count == 0:
                if (j - i + 1) < min_len:
                    min_len = j - i + 1
                    start_index = i
                
                if s[i] in d:
                    d[s[i]] += 1
                    if d[s[i]] > 0:
                        count += 1
                
                i += 1

            j += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[start_index : start_index + min_len]