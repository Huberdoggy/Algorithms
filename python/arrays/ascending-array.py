"""
You are given an array of integers a. A new array b is generated by
rearranging the elements of a in the following way:

b[0] is equal to a[0];
b[1] is equal to the last element of a;
b[2] is equal to a[1];
b[3] is equal to the second-last element of a;
b[4] is equal to a[2];
b[5] is equal to the third-last element of a; and so on.
Your task is to determine whether the new array
b is sorted in strictly ascending order or not.

Example

For a = [1, 3, 5, 6, 4, 2], the output should be solution(a) = true.
The new array b will look like [1, 2, 3, 4, 5, 6], which is in strictly ascending order,
so the answer is true.
For a = [1, 4, 5, 6, 3], the output should be solution(a) = false.
The new array b will look like [1, 3, 4, 6, 5], which is not in strictly ascending order, so the answer is false.
"""


def is_ascending(a):
    b = []
    i, j = 0, -1
    while i < len(a) - 2:
        b.append(a[i])
        b.append(a[j])
        i += 1
        j -= 1

    diff = len(b) - len(a)
    if diff != 0:
        # Start offset at the inverse of 'diff'
        del b[-diff:]

    """
    I believe O(2n) complexity - single iteration over elements of 'a'
    followed by subsequent slice (which is considered a copy operation)
    Dropping irrelevant constant yields O(n)
    """

    print(b)
    for count in range(b[0], b[-1] + 1, 1):
        if count not in b:
            return False
    return True


print(is_ascending([1, 3, 5, 6, 4, 2]))
print(is_ascending([1, 4, 5, 6, 3]))