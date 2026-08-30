class NumArray:
    def __init__(self, nums: list[int]):
        """
        Example: nums = [-2, 0, 3, -5, 2, -1]

        1. Define prefix = [0] * (len(nums) + 1)
        2. For i, num in enumerate(nums):
            2.1 Set prefix[i + 1] = prefix[i] + num
        3. Store prefix on self

        Complexity:
            Time complexity: O(n); where n is the size of nums
            Space complexity: O(n); where n is the size of nums
        """
        # T | S
        self.prefix = [0] * (len(nums) + 1)  # O(n) | O(n)

        for i, num in enumerate(nums):  # O(n) | O(1)
            self.prefix[i + 1] = self.prefix[i] + num  # O(1) | O(1)

    def sumRange(self, left: int, right: int) -> int:
        """
        Example: prefix = [0, -2, -2, 1, -4, -2, -3], left = 2, right = 5

        1. return prefix[right + 1] - prefix[left]

        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        return self.prefix[right + 1] - self.prefix[left]  # O(1) | O(1)


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Example: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    1. Define groups = {}
    2. For each s in strs:
        2.1 Define count_array = [0] * 26
        2.2 For each c in s: increment count_array[ord(c) - ord('a')]
        2.3 Get key = tuple(count_array)
        2.4 If key already in groups: append s to groups[key]
        2.5 Otherwise: groups[key] = [s]
    3. return list(groups.values())

    Complexity:
        Time complexity: O(n * k); where n is the number of strings and k is the max string length
        Space complexity: O(n); where n is the number of strings
    """
    # T | S
    groups = {}  # O(1) | O(1)

    for s in strs:  # O(n) | O(1)
        count_array = [0] * 26  # O(1) | O(1)

        for c in s:  # O(k) | O(1)
            count_array[ord(c) - ord("a")] += 1  # O(1) | O(1)

        key = tuple(count_array)  # O(1) | O(1)

        if key in groups:  # O(1) | O(1)
            groups[key].append(s)  # O(1) | O(1)
        else:
            groups[key] = [s]  # O(1) | O(1)

    return list(groups.values())  # O(n) | O(n)


def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """
    Example: matrix = [[1,2,3],[4,5,6],[7,8,9]]

    1. Define result = []
    2. Define boundaries top = 0, bottom = len(matrix) - 1, left = 0, right = len(matrix[0]) - 1
    3. While top <= bottom and left <= right:
        3.1 Traverse the top row from left to right; then top += 1
        3.2 Traverse the right column from top to bottom; then right -= 1
        3.3 If top <= bottom: traverse the bottom row from right to left; then bottom -= 1
        3.4 If left <= right: traverse the left column from bottom to top; then left += 1
    4. return result

    Complexity:
        Time complexity: O(m * n); where m, n are the matrix dimensions
        Space complexity: O(m * n); where m, n are the matrix dimensions
    """
    # T | S
    result = []  # O(1) | O(1)
    top = 0  # O(1) | O(1)
    bottom = len(matrix) - 1  # O(1) | O(1)
    left = 0  # O(1) | O(1)
    right = len(matrix[0]) - 1  # O(1) | O(1)

    while top <= bottom and left <= right:  # O(m * n) | O(m * n)
        for c in range(left, right + 1):  # O(n) | O(n)
            result.append(matrix[top][c])  # O(1) | O(1)

        top += 1  # O(1) | O(1)

        for r in range(top, bottom + 1):  # O(m) | O(m)
            result.append(matrix[r][right])  # O(1) | O(1)

        right -= 1  # O(1) | O(1)

        if top <= bottom:  # O(1) | O(1)
            for c in range(right, left - 1, -1):  # O(n) | O(n)
                result.append(matrix[bottom][c])  # O(1) | O(1)

            bottom -= 1  # O(1) | O(1)

        if left <= right:  # O(1) | O(1)
            for r in range(bottom, top - 1, -1):  # O(m) | O(m)
                result.append(matrix[r][left])  # O(1) | O(1)

            left += 1  # O(1) | O(1)

    return result  # O(1) | O(1)


def findAnagrams(s: str, p: str) -> list[int]:
    """
    Example: s = "cbaebabacd", p = "abc"

    1. Define result = []
    2. If len(s) < len(p): return result (p can't fit inside s)
    3. Define s_count = [0] * 26, p_count = [0] * 26
    4. For each c in p: increment p_count[ord(c) - ord('a')]
    5. Define left = 0, right = len(p) - 1 (the window [left, right] always has size len(p))
    6. For i in range(len(s)):
        6.1 Increment s_count for s[i] (grow the window on the right)
        6.2 If i > right: decrement s_count for s[left], then advance left and right by 1 (slide the window)
        6.3 If s_count == p_count: append left to result (window [left, right] is an anagram of p)
    7. return result

    Complexity:
        Time complexity: O(n); where n is the length of s
        Space complexity: O(n - k); where n is the length of s and k is the length of p
    """
    # T | S
    result = []  # O(1) | O(1)

    if len(s) < len(p):  # O(1) | O(1)
        return result  # O(1) | O(1)

    s_count = [0] * 26  # O(1) | O(1)
    p_count = [0] * 26  # O(1) | O(1)

    for c in p:  # O(k) | O(1)
        p_count[ord(c) - ord("a")] += 1  # O(1) | O(1)

    left = 0  # O(1) | O(1)
    right = len(p) - 1  # O(1) | O(1)
    for i in range(len(s)):  # O(n) | O(n - k)
        s_count[ord(s[i]) - ord("a")] += 1  # O(1) | O(1)

        if i > right:  # O(1) | O(1)
            s_count[ord(s[left]) - ord("a")] -= 1  # O(1) | O(1)
            left += 1  # O(1) | O(1)
            right += 1  # O(1) | O(1)

        if s_count == p_count:  # O(1) | O(1)
            result.append(left)  # O(1) | O(1)

    return result  # O(1) | O(1)


def subarraySum(nums: list[int], k: int) -> int:
    """
    Example: nums = [1, 2, 3, -2, 5], k = 5

    1. Define count = 0
    2. Define current_sum = 0
    3. Define seen = {0: 1} (prefix sum 0 occurs once, before any element)
    4. For each num in nums:
        4.1 current_sum += num
        4.2 count += seen.get(current_sum - k, 0) (each occurrence is a subarray ending here that sums to k)
        4.3 seen[current_sum] = seen.get(current_sum, 0) + 1
    5. return count

    Complexity:
        Time complexity: O(n); where n is the size of nums
        Space complexity: O(n); where n is the size of nums
    """
    # T | S
    count = 0  # O(1) | O(1)
    current_sum = 0  # O(1) | O(1)
    seen = {0: 1}  # O(1) | O(1)

    for num in nums:  # O(n) | O(n)
        current_sum += num  # O(1) | O(1)
        count += seen.get(current_sum - k, 0)  # O(1) | O(1)
        seen[current_sum] = seen.get(current_sum, 0) + 1  # O(1) | O(1)

    return count  # O(1) | O(1)


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Example: nums = [2, 7, 11, 15], target = 9

    1. Define seen_numbers = {}
    2. Define complement = 0
    3. For index, current_number in enumerate(nums):
        3.1 Set complement = target - current_number
        3.2 If complement in seen_numbers: return [seen_numbers[complement], index]
        3.3 Set seen_numbers[current_number] = index
    4. return []

    Complexity:
        Time complexity: O(n); where n is the size of nums
        Space complexity: O(n); where n is the size of nums
    """
    # T | S
    seen_numbers = {}  # O(1) | O(1)
    complement = 0  # O(1) | O(1)

    for index, current_number in enumerate(nums):  # O(n) | O(n)
        complement = target - current_number  # O(1) | O(1)

        if complement in seen_numbers:  # O(1) | O(1)
            return [seen_numbers[complement], index]  # O(1) | O(1)

        seen_numbers[current_number] = index  # O(1) | O(1)

    return []  # O(1) | O(1)


def twoSumBruteForce(nums: list[int], target: int) -> list[int]:
    """
    Example: nums = [2, 7, 11, 15], target = 9

    1. For i in range(len(nums)):
        1.1 For j in range(i + 1, len(nums)):
            1.1.1 If nums[i] + nums[j] == target: return [i, j]
    2. return []

    Complexity:
        Time complexity: O(n^2); where n is the size of nums
        Space complexity: O(1);
    """
    # T | S
    for i in range(len(nums)):  # O(n^2) | O(1)
        for j in range(i + 1, len(nums)):  # O(n) | O(1)
            if nums[i] + nums[j] == target:  # O(1) | O(1)
                return [i, j]  # O(1) | O(1)

    return []  # O(1) | O(1)
