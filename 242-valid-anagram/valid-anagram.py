class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}

        if len(s) != len(t):  # If lengths differ, they cannot be anagrams
            return False

        # Count occurrences of each letter in 's'
        for letter in s:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Subtract occurrences based on letters in 't'
        for letter in t:
            if letter in letter_count:
                letter_count[letter] -= 1
                if letter_count[letter] < 0:  # More occurrences in 't' than in 's'
                    return False
            else:
                return False  # Letter in 't' not found in 's'

        return True  # All counts should be zero if it's an anagram
