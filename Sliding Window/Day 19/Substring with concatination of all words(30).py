from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        word_count = len(words)
        
        # This is the dictionary tracking how many of each word we need
        target_dict = Counter(words)
        result = []
        
        # The brilliant outer loop: running 'word_len' separate tracks
        for offset in range(word_len):
            i = offset
            j = offset
            seen_words = Counter()
            count = 0
            
            # Slide the window across this specific track
            while j + word_len <= len(s):
                # Extract the current word and immediately jump j forward
                current_word = s[j : j + word_len]
                j += word_len
                
                # Case 1 & 2: The word is valid and in our target list
                if current_word in target_dict:
                    seen_words[current_word] += 1
                    count += 1
                    
                    # Case 3: We have TOO MANY of this valid word. Time to shrink!
                    while seen_words[current_word] > target_dict[current_word]:
                        left_word = s[i : i + word_len]
                        seen_words[left_word] -= 1
                        count -= 1
                        i += word_len  # i jumps forward by word_len too!
                    
                    # If our valid word count matches the required number of words, we win!
                    if count == word_count:
                        result.append(i)
                        
                # Case 4: Streak broken! The word is junk.
                else:
                    seen_words.clear()
                    count = 0
                    i = j  # Snap the start pointer right to where j is
                    
        return result