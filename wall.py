# Brick Wall
#
# You have an unlimited number of bricks that are of length 1, 2, 3, and 4.
# You are going to construct a wall of height `n` and width `m` by stacking these bricks on top of and next to each other.
# The bricks cannot be laid vertically (so the height of the wall will only go up by 1 when you lay a brick).
#
# A wall is valid if:
# - It is one solid structure, there is not a vertical break from top to bottom across bricks
# - There are no holes in the wall
#
# There are going to be a very large number of possible walls at higher values.
# Output the number of possible wall combinations modulo 1000000007.
#
# `n` and `m` can range anywhere between 1 and 1000.


import time, sys

# Python recursion depth limit is usually 1000,
# which presents an issue for a recursive solution to this problem.
# However, the problem constraints mean we can increase the limit without worrying.
sys.setrecursionlimit(1010)


BRICK_LENGTHS = (1,2,3,4)
row_perms = {0: 1}
wall_perms = {}
valid_wall_perms = {1: 1}


def count_rows(remaining_width):
    stored = row_perms.get(remaining_width)
    if stored:
        return stored
    sum = 0
    for brick in BRICK_LENGTHS:
        if brick <= remaining_width:
            sum = (sum + count_rows(remaining_width-brick)) % 1000000007
    row_perms[remaining_width] = sum
    return row_perms[remaining_width]


def all_walls(height, width):
    stored = wall_perms.get(width)
    if stored:
        return stored
    wall_perms[width] = pow(count_rows(width), height, 1000000007)
    return wall_perms[width]


def count_walls(height, width):
    stored = valid_wall_perms.get(width)
    if stored:
        return stored
    sum = 0
    for i in range(1, width):
        sum += (count_walls(height, i) * all_walls(height, width-i)) % 1000000007
    sum = sum % 1000000007
    valid_wall_perms[width] = (all_walls(height, width) - sum) % 1000000007
    return valid_wall_perms[width]
    

try:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
except IndexError:
    print("ERROR: 2 arguments are required")
except ValueError:
    print("ERROR: one or more arguments are not integers")
else:
    if not (1 <= n <= 1000 and 1 <= m <= 1000):
        print("ERROR: arguments must be between 1 and 1000 (inclusive)")
    else:
        print(count_walls(n, m))
