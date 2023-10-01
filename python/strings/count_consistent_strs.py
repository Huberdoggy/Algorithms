"""
You are given a string allowed consisting of distinct
characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent
since they only contain characters 'a' and 'b'.
"""


class Solution:
    def __init__(self) -> None:
        self.consistent = {}

    def check_current_word(self, curr_el: str) -> int:
        tmp_count = 0
        for i in range(len(curr_el)):
            if curr_el[i] in self.consistent.values():
                tmp_count += 1  # Temporary - is each letter in dict??
        # Eval entire word is consistent, since we're iterating each char here
        return (tmp_count := 1 if tmp_count == len(curr_el) else 0)

    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        for char in range(len(allowed)):
            if allowed[char] not in self.consistent:
                self.consistent[char] = str(allowed[char])

        res = 0  # To hold total num of consistent strs
        for i in range(len(words)):
            curr_el = words[i]
            count = self.check_current_word(curr_el)
            res += count

        return res


x = Solution()
print(x.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
