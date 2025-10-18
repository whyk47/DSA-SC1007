# Q1a: When every element of L is the last element of M
# b: Suppose the # of elements in L and M are a and b respectively. 
# Total comparisons = ab
# c: f(a, b) = c0 + a(c1 + bc2)
# d: O(ab)

# Q2a: Inner loop: N/2, Outer loop: N/3, total: N^2/6, O(N^2)
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
