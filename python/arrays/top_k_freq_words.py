"""
Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most
frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
"""


class Solution:
    def __init__(self) -> None:
        pass

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequencies, top = {}, []
        count = 0
        for i in range(len(words)):
            if words[i] not in frequencies:
                frequencies[f"{words[i]}"] = 1
            else:
                frequencies[f"{words[i]}"] += 1

        # The '1' index references 'value' in lambda iter of dict
        # So, '0' will yield the key
        # print(entry[0], ":", entry[1])
        frequencies = [
            entry
            for entry in sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        ]

        print(frequencies)

        while count < k:
            top.append(frequencies[count][0])  # Ref to str key of each tuple item
            count += 1

        print(top)
        # return


x = Solution()
print(x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(
    x.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    )
)
# TODO - 'coding' needs to be in output instead of 'leetcode' due to alphatbetical
# Despite same frequency
print(x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
