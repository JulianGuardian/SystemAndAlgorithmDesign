def search(nums: list[int], target: int) -> int:
    """
    Example: nums = [-1, 0, 3, 5, 9, 12], target = 9

    1. Define left = 0
    2. Define right = len(nums) - 1
    3. While left <= right:
        3.1 Get the middle = (left + right) // 2
        3.2 If nums[middle] == target: return middle
        3.3 If nums[middle] < target: left = middle + 1
        3.4 Otherwise: right = middle - 1
    4. return -1

    Complexity:
        Time complexity: O(log n); where n is the size of the array
        Space complexity: O(1)
    """
    # T | S
    left = 0  # O(1) | O(1)
    right = len(nums) - 1  # O(1) | O(1)

    while left <= right:  # O(log n) | O(1)
        mid = left + (right - left) // 2  # O(1) | O(1)

        if nums[mid] == target:  # O(1) | O(1)
            return mid  # O(1) | O(1)
        elif nums[mid] < target:  # O(1) | O(1)
            left = mid + 1  # O(1) | O(1)
        else:
            right = mid - 1  # O(1) | O(1)

    return -1  # O(1) | O(1)


def twoSum(numbers: list[int], target: int) -> list[int]:
    """
    Example: numbers = [2, 7, 11, 15], target = 9

    1. Define left = 0
    2. Define right = len(numbers) - 1
    3. While left < right:
        3.1 Get temporal_sum = numbers[left] + numbers[right]
        3.2 If temporal_sum == target: return [left + 1, right + 1]
        3.3 If temporal_sum > target: right = right - 1
        3.4 Otherwise: left = left + 1
    4. return []

    Complexity:
        Time complexity: O(n); where n is the size of the array
        Space complexity: O(1)
    """
    # T | S
    left = 0  # O(1) | O(1)
    right = len(numbers) - 1  # O(1) | O(1)

    while left < right:  # O(n) | O(1)
        temporal_sum = numbers[left] + numbers[right]  # O(1) | O(1)

        if temporal_sum == target:  # O(1) | O(1)
            return [left + 1, right + 1]  # O(1) | O(1)
        elif temporal_sum > target:  # O(1) | O(1)
            right = right - 1  # O(1) | O(1)
        else:
            left = left + 1  # O(1) | O(1)

    return []  # O(1) | O(1)


def lengthOfLongestSubstring(s: str) -> int:
    """
    Example: s = "abcabcbb"

    1. Define seen = [-1 for _ in range(128)] (last index where each ASCII character appeared; -1 means "not seen yet")
    2. Define left = 0
    3. Define max_length = 0
    4. For each right, char in enumerate(s):
        4.1 Get ascii_index = ord(char)
        4.2 If seen[ascii_index] >= left: left = seen[ascii_index] + 1
        4.3 Set seen[ascii_index] = right
        4.4 Update max_length = max(max_length, right - left + 1)
    5. return max_length

    Complexity:
        Time complexity: O(n); where n is the length of the string
        Space complexity: O(1); seen is a fixed-size array (128 for ASCII)
    """
    # T | S
    seen = [-1 for _ in range(128)]  # O(1) | O(1)
    left = 0  # O(1) | O(1)
    max_length = 0  # O(1) | O(1)

    for right, char in enumerate(s):  # O(n) | O(1)
        ascii_index = ord(char)  # O(1) | O(1)
        if seen[ascii_index] >= left:  # O(1) | O(1)
            left = seen[ascii_index] + 1  # O(1) | O(1)
        seen[ascii_index] = right  # O(1) | O(1)
        max_length = max(max_length, right - left + 1)  # O(1) | O(1)

    return max_length  # O(1) | O(1)


def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
    Example: target = 7, nums = [2, 3, 1, 2, 4, 3]

    1. Define min_length = infinity
    2. Define left = 0
    3. Define actual_sum = 0
    4. For right in range(len(nums)):
        4.1 actual_sum += nums[right]
        4.2 While actual_sum >= target:
            4.2.1 Update min_length = min(min_length, right - left + 1)
            4.2.2 actual_sum -= nums[left]
            4.2.3 left += 1
    5. If min_length == infinity: return 0
    6. return min_length

    Complexity:
        Time complexity: O(n); where n is the size of the array.
        Space complexity: O(1)
    """
    # T | S
    min_length = float("inf")  # O(1) | O(1)
    left = 0  # O(1) | O(1)
    actual_sum = 0  # O(1) | O(1)

    for right in range(len(nums)):  # O(n) | O(1)
        actual_sum += nums[right]  # O(1) | O(1)

        while (
            actual_sum >= target
        ):  # O(1) amortized (O(n) total across the whole run) | O(1)
            min_length = min(min_length, right - left + 1)  # O(1) | O(1)

            actual_sum -= nums[left]  # O(1) | O(1)
            left += 1  # O(1) | O(1)

    if min_length == float("inf"):  # O(1) | O(1)
        return 0  # O(1) | O(1)

    return min_length  # O(1) | O(1)


def findMin(nums: list[int]) -> int:
    """
    Example: nums = [3, 4, 5, 1, 2]

    1. Define left = 0
    2. Define right = len(nums) - 1
    3. While left != right:
        3.1 Get middle = (left + right) / 2
        3.2 If nums[middle] < nums[left]: right = middle (minimum is in the left half)
        3.3 If nums[middle] > nums[right]: left = middle + 1 (minimum is in the right half)
        3.4 Otherwise: return nums[left] (this segment is already sorted)
    4. return nums[left]

    Complexity:
        Time complexity: O(log n); where n is the size of the array
        Space complexity: O(1)
    """
    # T | S
    left = 0  # O(1) | O(1)
    right = len(nums) - 1  # O(1) | O(1)

    while left != right:  # O(log n) | O(1)
        mid = left + (right - left) // 2  # O(1) | O(1)

        if nums[mid] < nums[left]:  # O(1) | O(1)
            right = mid  # O(1) | O(1)
        elif nums[mid] > nums[right]:  # O(1) | O(1)
            left = mid + 1  # O(1) | O(1)
        else:
            return nums[left]  # O(1) | O(1)

    return nums[left]  # O(1) | O(1)


def searchInsert(nums: list[int], target: int) -> int:
    """
    Example: nums = [1, 3, 5, 6], target = 5

    1. Define left = 0
    2. Define right = len(nums) - 1
    3. While left <= right:
        3.1 Get middle = left + (right - left) // 2
        3.2 If nums[middle] == target: return middle
        3.3 If nums[middle] < target: left = middle + 1
        3.4 Otherwise: right = middle - 1
    4. return left (insertion point once the search space is exhausted)

    Complexity:
        Time complexity: O(log n); where n is the size of the array
        Space complexity: O(1)
    """
    # T | S
    left = 0  # O(1) | O(1)
    right = len(nums) - 1  # O(1) | O(1)

    while left <= right:  # O(log n) | O(1)
        mid = left + (right - left) // 2  # O(1) | O(1)

        if nums[mid] == target:  # O(1) | O(1)
            return mid  # O(1) | O(1)
        elif nums[mid] < target:  # O(1) | O(1)
            left = mid + 1  # O(1) | O(1)
        else:
            right = mid - 1  # O(1) | O(1)

    return left  # O(1) | O(1)