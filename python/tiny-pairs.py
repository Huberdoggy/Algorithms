"""
"You are given two arrays of integers a and b of the same length, and an integer k.
We will be iterating through array a from left to right, and simultaneously through array
b from right to left, and looking at pairs (x, y), where x is from a and y is from b.
Such a pair is called tiny if the concatenation xy is strictly less than k
"""


def find_pairs(a, b, k):
    seen = set()
    if len(a) == 0 or len(b) == 0:
        return 0

    for i, x in enumerate(a):
        for j, y in reversed(list(enumerate(b))):
            if int(x) + int(y) < int(k):
                # print(f"X is {x} and y is {y}")
                seen.add(int(x) + int(y))
    print(seen)
    return len(seen)


print(find_pairs([1, 2, 3], [1, 2, 3], 4))
print(find_pairs([], [], 4))
print(find_pairs([1, 2, 3], [], 10))
print(find_pairs([], [1, 2, 3], 8))
