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
frequent words, with the number of ocfrequenciesence being 4, 3, 2 and 1 respectively.
"""


class Solution:
    def __init__(self) -> None:
        pass

    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        frequencies, top = {}, []
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

        start, end = 0, len(frequencies) - 1
        while start < k:
            if frequencies[start][1] == frequencies[end][1]:
                top.append(
                    min(frequencies[start][0], frequencies[end][0])
                )  # Ref to str key of each tuple item
            else:
                top.append(frequencies[start][0])
            start += 1
            # 'End' is never moving, so, each iteration, if the freqs are not equal,
            # the str val of the sorted tuple will be appended in correct descending order
            # Else, the lexographically lowest will be chosen (aka 'coding' before 'leetcode')
        return top


x = Solution()
print(x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(
    x.topKFrequent(
        ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4
    )
)
print(x.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
