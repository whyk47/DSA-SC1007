# Q1a: Let |L| = a and |M| = b
# When the 1st a-1 elements from L are the last a-1 elements from M in reverse order, 
# and the last element in L is not in M
# b: total comparisons = b + b-1 + ... + b-a-2 + b = ab - (1+2+...+a-2)
#                      = ab - (a-2)/2 * (a-1) = theta(ab)
# c: f(a, b) = ab - (a-2)/2 * (a-1)
# d: theta(ab)

# Q2a: let M be the last iteration of the inner loop
# 2^(M-1) <= N, M-1 <= log2(N)
# Since M is an integer, M = floor(log2(n) + 1)
# Similarly, let H be the last iteration of the outer loop
# H = floor(log3(n) + 1) 
# total: floor(log2(n) + 1) * floor(log3(n) + 1) = theta(log(N)^2)

# Q2b: W(N) = N + 2W(N-1) = N + 2(N-1 + 2W(N-2)) = N + 2(N-1) + 4W(N-3)
#           = ... = N + 2(N-1) + 2^2 * (N-2) + ... + 2^(N-1) * (1) 
#           = Summation from 0 to N-1 (2^k * (N-k))
#           = N * Summation from 0 to N-1 (2^k) - Summation from 0 to N-1 (k * 2^k)
#           = N * (2^N - 1) - 2 * (2^(N-1) * (N - 2) + 1)
#           = N * 2^N - N - 2^N * (N-2) - 2 
#           = 2^(N+1) - N - 2 = O(2^N)

from typing import Sequence


def find_min_cyclic_sort(nums: Sequence[int], start: int, end: int) -> int:
    if start == end:
        return nums[start]
    mid = (start + end) // 2
    if nums[mid] <= nums[mid - 1] and nums[mid] <= nums[(mid + 1) % len(nums)]:
        return nums[mid]
    if nums[mid] <= nums[end]:
        return find_min_cyclic_sort(nums, start, mid - 1)
    else:
        return find_min_cyclic_sort(nums, mid + 1, end)

print(find_min_cyclic_sort("6712345", 0, 6))
print(find_min_cyclic_sort("3456712", 0, 6))
