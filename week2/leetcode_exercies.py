def subsets(nums: list[int]) -> list[list[int]]:
    """
    Example: nums = [1, 2, 3]

    1. Define results = []
    2. Define backtrack(start, current):
        2.1 Append a copy of current to results
        2.2 For i in range(start, len(nums)):
            2.2.1 Append nums[i] to current
            2.2.2 backtrack(i + 1, current)
            2.2.3 Remove the last element from current (backtrack)
    3. backtrack(0, [])
    4. return results

    Complexity:
        Time complexity: O(n * 2^n); where n is the size of nums
        Space complexity: O(n * 2^n); where n is the size of nums
    """
    # T | S
    results = []  # O(1) | O(1)

    def backtrack(start: int, current: list[int]):
        results.append(list(current))  # O(n) | O(n)

        for i in range(start, len(nums)):  # O(n) | O(1)
            current.append(nums[i])  # O(1) | O(1)
            backtrack(i + 1, current)  # O(2^n) | O(n) tree and O(2^n) output
            current.pop()  # O(1) | O(1)

    backtrack(0, [])  # O(n * 2^n) | O(n * 2^n)
    return results  # O(1) | O(1)


def permute(nums: list[int]) -> list[list[int]]:
    """
    Example: nums = [1, 2, 3]

    1. Define results = []
    2. Define backtrack(current, remaining):
        2.1 If remaining is empty: append a copy of current to results; return
        2.2 For i in range(len(remaining)):
            2.2.1 Append remaining[i] to current
            2.2.2 backtrack(current, remaining without index i)
            2.2.3 Remove the last element from current (backtrack)
    3. backtrack([], nums)
    4. return results

    Complexity:
        Time complexity: O(n * n!); where n is the size of nums
        Space complexity: O(n * n!); where n is the size of nums
    """
    # T | S
    results = []  # O(1) | O(1)

    def backtrack(current: list[int], remaining: list[int]):
        if not remaining:  # O(1) | O(1)
            results.append(list(current))  # O(n) | O(n)
            return  # O(1) | O(1)

        for i in range(len(remaining)):  # O(n) | O(1)
            current.append(remaining[i])  # O(1) | O(1)
            backtrack(
                current, remaining[:i] + remaining[i + 1 :]
            )  # O(n!) | O(n^2) tree and O(n!) output
            current.pop()  # O(1) | O(1)

    backtrack([], nums)  # O(n * n!) | O(n * n!)
    return results  # O(1) | O(1)


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Example: candidates = [2, 3, 6, 7], target = 7

    1. Define results = []
    2. Define backtrack(start, current):
        2.1 If sum(current) == target: append a copy of current to results; return
        2.2 If sum(current) > target: return (prune)
        2.3 For i in range(start, len(candidates)):
            2.3.1 Append candidates[i] to current
            2.3.2 backtrack(i, current) (reusing the same candidate is allowed)
            2.3.3 Remove the last element from current (backtrack)
    3. backtrack(0, [])
    4. return results

    Complexity:
        Time complexity: O(n^t); where n is the size of candidates and t is the target
        Space complexity: O(t * n^t); where n is the size of candidates and t is the target
    """
    # T | S
    results = []  # O(1) | O(1)

    def backtrack(start: int, current: list[int]):
        sum_value = sum(current)  # O(t) | O(1)

        if sum_value == target:  # O(1) | O(1)
            results.append(list(current))  # O(t) | O(t)
            return  # O(1) | O(1)

        if sum_value > target:  # O(1) | O(1)
            return  # O(1) | O(1)

        for i in range(start, len(candidates)):  # O(n) | O(1)
            current.append(candidates[i])  # O(1) | O(1)
            backtrack(i, current)  # O(n^t) | O(t) tree and O(n^t) output
            current.pop()  # O(1) | O(1)

    backtrack(0, [])  # O(n^t) | O(t * n^t)
    return results  # O(1) | O(1)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode | None) -> ListNode | None:
    """
    Example: head = [1,2,3,4,5]

    1. Define prev = None
    2. Define current = head
    3. While current:
        3.1 Get actual_next_node = current.next
        3.2 Set current.next = prev
        3.3 Set prev = current
        3.4 Set current = actual_next_node
    4. return prev

    Complexity:
        Time complexity: O(n); where n is the number of nodes in the list
        Space complexity: O(1)
    """
    # T | S
    prev = None  # O(1) | O(1)
    current = head  # O(1) | O(1)

    while current:  # O(n) | O(1)
        actual_next_node = current.next  # O(1) | O(1)
        current.next = prev  # O(1) | O(1)
        prev = current  # O(1) | O(1)
        current = actual_next_node  # O(1) | O(1)

    return prev  # O(1) | O(1)


def reverseListRecursive(head: ListNode | None) -> ListNode | None:
    """
    Example: head = [1,2,3,4,5]

    1. Define backtrack(prev, current):
        1.1 If current is None: return prev (base case, reached the end)
        1.2 Get actual_next_node = current.next
        1.3 Set current.next = prev
        1.4 return backtrack(current, actual_next_node)
    2. return backtrack(None, head)

    Complexity:
        Time complexity: O(n); where n is the number of nodes in the list
        Space complexity: O(n); recursion call stack depth for n nodes
    """

    # T | S
    def backtrack(prev: ListNode | None, current: ListNode | None) -> ListNode | None:
        if not current:  # O(1) | O(1)
            return prev  # O(1) | O(1)

        actual_next_node = current.next  # O(1) | O(1)
        current.next = prev  # O(1) | O(1)

        return backtrack(current, actual_next_node)  # O(n) | O(n)

    return backtrack(None, head)  # O(n) | O(n)


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    """
    Example: nums = [1, 2, 2]

    1. Sort nums (so duplicates become adjacent)
    2. Define results = []
    3. Define backtrack(start, current):
        3.1 Append a copy of current to results
        3.2 For i in range(start, len(nums)):
            3.2.1 If i > start and nums[i] == nums[i - 1]: skip (avoid a duplicate branch)
            3.2.2 Append nums[i] to current
            3.2.3 backtrack(i + 1, current)
            3.2.4 Remove the last element from current (backtrack)
    4. backtrack(0, [])
    5. return results

    Complexity:
        Time complexity: O(n * 2^n); where n is the size of nums
        Space complexity: O(n * 2^n); where n is the size of nums
    """
    # T | S
    results = []  # O(1) | O(1)
    nums.sort()  # O(n log n) | O(1)

    def backtrack(start: int, current: list[int]):
        results.append(list(current))  # O(n) | O(n)

        for i in range(start, len(nums)):  # O(n) | O(1)
            if i > start and nums[i] == nums[i - 1]:  # O(1) | O(1)
                continue  # O(1) | O(1)

            current.append(nums[i])  # O(1) | O(1)
            backtrack(i + 1, current)  # O(2^n) | O(n) tree and O(2^n) output
            current.pop()  # O(1) | O(1)

    backtrack(0, [])  # O(n * 2^n) | O(n * 2^n)
    return results  # O(1) | O(1)


def combine(n: int, k: int) -> list[list[int]]:
    """
    Example: n = 4, k = 2

    1. Define results = []
    2. Define backtrack(start, current):
        2.1 If len(current) == k: append a copy of current to results; return
        2.2 Compute limit = n - (k - len(current)) + 2
            (the largest i we could still start from and have enough
            numbers left, up to n, to complete a combination of size k)
        2.3 For i in range(start, limit):
            2.3.1 Append i to current
            2.3.2 backtrack(i + 1, current)
            2.3.3 Remove the last element from current (backtrack)
    3. backtrack(1, [])
    4. return results

    Pruning explanation:
        Without the limit, the loop would run all the way to n even when
        there aren't enough remaining numbers left to fill out a
        combination of size k, wasting calls that can never reach the
        base case. With `need = k - len(current)` numbers still required,
        the last valid starting value is `n - need + 1`, so the
        (exclusive) upper bound is `n - need + 2`. This skips branches
        that are guaranteed to fail early instead of discovering it one
        level (or more) deeper in the recursion.

    Complexity:
        Time complexity: O(k * C(n, k)); where C(n, k) is the number of combinations and k is the cost to copy each one into results
        Space complexity: O(k * C(n, k)); where C(n, k) is the number of combinations and k is the size of each combination
    """
    # T | S
    results = []  # O(1) | O(1)

    def backtrack(start: int, current: list[int]):
        if len(current) == k:  # O(1) | O(1)
            results.append(list(current))  # O(k) | O(k)
            return  # O(1) | O(1)

        limit = n - (k - len(current)) + 2  # O(1) | O(1)

        for i in range(start, limit):  # O(n) | O(1)
            current.append(i)  # O(1) | O(1)
            backtrack(i + 1, current)  # O(C(n,k)) | O(k) tree and O(k * C(n,k)) output
            current.pop()  # O(1) | O(1)

    backtrack(1, [])  # O(k * C(n, k)) | O(k * C(n, k))
    return results  # O(1) | O(1)
