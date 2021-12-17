#!/usr/bin/env python3
import sys
import math
import random
import functools
import itertools
import collections
import heapq
import bisect
from collections import Counter, defaultdict, deque
# input = sys.stdin.readline  # to read input quickly


M = 10**9 + 7
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
MININT = -MAXINT - 1


def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


def read_strings(rows):
    return [input().strip() for _ in range(rows)]


def minus_one(arr):
    return [x-1 for x in arr]


def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------


class Solution():
    def solve():
        # read line as an integer
        # k = int(input())

        # read line as a string
        # srr = input().strip()

        # read one line and parse each word as a string
        # lst = input().split()

        # read one line and parse each word as an integer
        # a,b,c = list(map(int,input().split()))
        # lst = list(map(int,input().split()))
        # lst = minus_one(lst)

        # read multiple rows
        # arr = read_strings(k)  # and return as a list of str
        # mrr = read_matrix(k)  # and return as a list of list of int
        # mrr = minus_one_matrix(mrr)

        # print length if applicable
        # print(len(res))

        # parse result
        # res = " ".join(str(x) for x in res)
        # res = "\n".join(str(x) for x in res)
        # res = "\n".join(" ".join(str(x) for x in row) for row in res)
        pass


if __name__ == "__main__":
    solution = Solution()
    solution.solve()