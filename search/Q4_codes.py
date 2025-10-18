def find_median_sorted_arrays(num1, num2):
    """
    Finds the median of two sorted arrays in O(log(m+n)) time complexity.

    Parameters:
    num1 (list): First sorted array.
    num2 (list): Second sorted array.

    Returns:
    float: The median of the combined sorted array.
    """
    if len(num1) > len(num2):
        num1, num2 = num2, num1  # Ensure num1 is the smaller array

    m, n = len(num1), len(num2)
    imin, imax, half_len = 0, m, (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and num1[i] < num2[j - 1]:
            imin = i + 1  # i is too small, move right
        elif i > 0 and num1[i - 1] > num2[j]:
            imax = i - 1  # i is too big, move left
        else:
            max_of_left = 0
            if i == 0:
                max_of_left = num2[j - 1]
            elif j == 0:
                max_of_left = num1[i - 1]
            else:
                max_of_left = max(num1[i - 1], num2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left  # Odd total length

            min_of_right = 0
            if i == m:
                min_of_right = num2[j]
            elif j == n:
                min_of_right = num1[i]
            else:
                min_of_right = min(num1[i], num2[j])

            return (max_of_left + min_of_right) / 2.0  # Even total length



num1 = [1, 3, 8]
num2 = [7, 9, 10, 11]
median = find_median_sorted_arrays(num1, num2)
print("Median of the two sorted arrays is:", median)