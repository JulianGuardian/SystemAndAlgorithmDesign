import heapq
from collections import Counter


def findKthLargest(nums: list[int], k: int) -> int:
    """
    Example: nums = [3,2,1,5,6,4], k = 2

    1. Define heap = nums[:k]
    2. Heapify heap (min-heap with the first k numbers; the root is the smallest of them)
    3. For number in nums[k:]:
        3.1 If number > heap[0]: replace the root with number (number belongs in the
            top k, and the old root is pushed out)
    4. return heap[0] (the heap holds the k largest numbers, so its root is the k-th largest)

    Complexity:
        Time complexity: O(n log k); where n is the length of nums - each of the n - k
            remaining numbers may cost one O(log k) replace
        Space complexity: O(k); the heap never holds more than k numbers
    """
    # T | S
    heap = nums[:k]  # O(k) | O(k)
    heapq.heapify(heap)  # O(k) | O(1)

    for number in nums[k:]:  # O(n - k) | O(n - k)
        if number > heap[0]:  # O(1) | O(1)
            heapq.heapreplace(heap, number)  # O(log k) | O(1)

    return heap[0]  # O(1) | O(1)


def topKFrequent(nums: list[int], k: int) -> list[int]:
    """
    Example: nums = [1,1,1,2,2,3], k = 2

    1. Define count = Counter(nums) (number -> frequency)
    2. Define heap = [] (min-heap of (frequency, number); the root is the least frequent
        number among the current top k)
    3. For number, frequency in count.items():
        3.1 Push (frequency, number) to heap
        3.2 If len(heap) > k: pop the root (the least frequent one is out of the top k)
    4. return [number for frequency, number in heap]

    Complexity:
        Time complexity: O(n log k); where n is the length of nums - counting is O(n) and
            each of the at most n distinct numbers costs O(log k) in the heap
        Space complexity: O(n); for count (the heap only holds k + 1 items)
    """
    # T | S
    count = Counter(nums)  # O(n) | O(n)
    heap = []  # O(1) | O(1)

    for number, frequency in count.items():  # O(n) | O(k)
        heapq.heappush(heap, (frequency, number))  # O(log k) | O(1)

        if len(heap) > k:  # O(1) | O(1)
            heapq.heappop(heap)  # O(log k) | O(1)

    return [number for frequency, number in heap]  # O(k) | O(k)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: list[ListNode | None]) -> ListNode | None:
    """
    Example: lists = [[1,4,5],[1,3,4],[2,6]]

    1. Define heap = []
    2. For index, node in enumerate(lists):
        2.1 If node: push (node.val, index, node) to heap (index breaks ties, so two
            ListNode objects are never compared)
    3. Define dummy = ListNode(0), actual = dummy
    4. While heap:
        4.1 Pop (value, index, node) (the smallest head among all lists)
        4.2 Set actual.next = node, then actual = actual.next
        4.3 If node.next: push (node.next.val, index, node.next) (that list's next candidate)
    5. return dummy.next

    Complexity:
        Time complexity: O(N log k); where N is the total number of nodes and k is the
            number of lists - every node is pushed and popped once, and the heap holds
            at most k nodes (one per list)
        Space complexity: O(k); for the heap (the result reuses the existing nodes)
    """
    # T | S
    heap = []  # O(1) | O(1)

    for index, node in enumerate(lists):  # O(k) | O(k)
        if node:  # O(1) | O(1)
            heapq.heappush(heap, (node.val, index, node))  # O(log k) | O(1)

    dummy = ListNode(0)  # O(1) | O(1)
    actual = dummy  # O(1) | O(1)

    while heap:  # O(N) | O(1)
        value, index, node = heapq.heappop(heap)  # O(log k) | O(1)
        actual.next = node  # O(1) | O(1)
        actual = actual.next  # O(1) | O(1)

        if node.next:  # O(1) | O(1)
            heapq.heappush(heap, (node.next.val, index, node.next))  # O(log k) | O(1)

    return dummy.next  # O(1) | O(1)


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    """
    Example: points = [[3,3],[5,-1],[-2,4]], k = 2

    1. Define heap = [] (max-heap simulated with negated squared distances; the root is
        the farthest point among the current k closest)
    2. For x, y in points:
        2.1 Push (-(x * x + y * y), x, y) to heap (no square root needed, squared
            distance keeps the same order)
        2.2 If len(heap) > k: pop the root (the farthest point is out of the k closest)
    3. return [[x, y] for distance, x, y in heap]

    Complexity:
        Time complexity: O(n log k); where n is the number of points
        Space complexity: O(k); the heap never holds more than k + 1 points
    """
    # T | S
    heap = []  # O(1) | O(1)

    for x, y in points:  # O(n) | O(k)
        heapq.heappush(heap, (-(x * x + y * y), x, y))  # O(log k) | O(1)

        if len(heap) > k:  # O(1) | O(1)
            heapq.heappop(heap)  # O(log k) | O(1)

    return [[x, y] for distance, x, y in heap]  # O(k) | O(k)


def lastStoneWeight(stones: list[int]) -> int:
    """
    Example: stones = [2,7,4,1,8,1]

    1. Define heap = [-stone for stone in stones] (negated to simulate a max-heap)
    2. Heapify heap
    3. While len(heap) > 1:
        3.1 Pop heaviest = -heappop(heap)
        3.2 Pop second = -heappop(heap)
        3.3 If heaviest != second: push -(heaviest - second) (the remainder survives)
    4. return -heap[0] if heap else 0

    Complexity:
        Time complexity: O(n log n); where n is the number of stones - each turn removes
            at least one stone and costs O(log n)
        Space complexity: O(n); for the heap
    """
    # T | S
    heap = [-stone for stone in stones]  # O(n) | O(n)
    heapq.heapify(heap)  # O(n) | O(1)

    while len(heap) > 1:  # O(n) | O(1)
        heaviest = -heapq.heappop(heap)  # O(log n) | O(1)
        second = -heapq.heappop(heap)  # O(log n) | O(1)

        if heaviest != second:  # O(1) | O(1)
            heapq.heappush(heap, -(heaviest - second))  # O(log n) | O(1)

    return -heap[0] if heap else 0  # O(1) | O(1)
