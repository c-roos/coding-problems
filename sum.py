# Integer Sum
#
# You are given a list of integers, and a single number.
# Identify a pair of integers from the list that sum to the single number.
# You only need to find one pair.


def find_pair(n, l):
    l.sort()
    left, right = 0, len(l)-1
    while right > left:
        sum = l[left] + l[right]
        if sum == n:
            return (l[left], l[right])
        elif sum < n:
            left += 1
        else:
            right -= 1
    return None
