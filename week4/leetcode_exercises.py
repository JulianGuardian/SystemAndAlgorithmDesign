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


def hasCycle(head: ListNode | None) -> bool:
    """
    Example: head = [3,2,0,-4] with the tail pointing back to node "2" (cycle)

    1. Define slow = head
    2. Define fast = head
    3. While fast and fast.next:
        3.1 Set fast = fast.next.next (fast advances two nodes)
        3.2 If fast == slow: return True (fast lapped slow inside the cycle)
        3.3 Set slow = slow.next (slow advances one node)
    4. return False (fast reached the end, so there's no cycle)

    Complexity:
        Time complexity: O(n); where n is the number of nodes in the list
        Space complexity: O(1)
    """
    # T | S
    slow = head  # O(1) | O(1)
    fast = head  # O(1) | O(1)

    while fast and fast.next:  # O(n) | O(1)
        fast = fast.next.next  # O(1) | O(1)

        if fast == slow:  # O(1) | O(1)
            return True  # O(1) | O(1)

        slow = slow.next  # O(1) | O(1)

    return False  # O(1) | O(1)


def mergeTwoLists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    """
    Example: list1 = [1,2,4], list2 = [1,3,4]

    1. Define dummy = ListNode(0), actual = dummy (dummy avoids a special case for the
        first node of the merged result)
    2. While list1 and list2:
        2.1 If list1.val < list2.val: set actual.next = list1, then list1 = list1.next
        2.2 Otherwise: set actual.next = list2, then list2 = list2.next
        2.3 Set actual = actual.next (advance the tail of the built-so-far result)
    3. Set actual.next = list1 if list1 else list2 (attach whichever list still has nodes left)
    4. return dummy.next (skip the dummy itself)

    Complexity:
        Time complexity: O(n + m); where n and m are the lengths of list1 and list2
        Space complexity: O(1)
    """
    # T | S
    dummy = ListNode(0)  # O(1) | O(1)
    actual = dummy  # O(1) | O(1)

    while list1 and list2:  # O(n + m) | O(1)
        if list1.val < list2.val:  # O(1) | O(1)
            actual.next = list1  # O(1) | O(1)
            list1 = list1.next  # O(1) | O(1)
        else:
            actual.next = list2  # O(1) | O(1)
            list2 = list2.next  # O(1) | O(1)

        actual = actual.next  # O(1) | O(1)

    actual.next = list1 if list1 else list2  # O(1) | O(1)
    return dummy.next  # O(1) | O(1)


def removeNthFromEnd(head: ListNode | None, n: int) -> ListNode | None:
    """
    Example: head = [1,2,3,4,5], n = 2

    1. Define start = head, end = head
    2. For i in range(n): advance end one node (opens an n-node gap between end and start)
    3. While end:
        3.1 If end.next is None: start is right before the target node
            3.1.1 Set start.next = start.next.next (skip the target node)
            3.1.2 return head
        3.2 Otherwise: advance both end and start one node (keep the n-node gap constant)
    4. return head.next (end became None during the gap-opening loop, so the head itself is the target)

    Complexity:
        Time complexity: O(m); where m is the number of nodes in the list
        Space complexity: O(1);
    """
    # T | S
    start = head  # O(1) | O(1)
    end = head  # O(1) | O(1)

    for i in range(n):  # O(n) | O(1)
        end = end.next  # O(1) | O(1)

    while end:  # O(m - n) | O(1)
        if end.next is None:  # O(1) | O(1)
            start.next = start.next.next  # O(1) | O(1)
            return head  # O(1) | O(1)

        end = end.next  # O(1) | O(1)
        start = start.next  # O(1) | O(1)

    return head.next  # O(1) | O(1)


class HashMapNode:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    """
    Separate chaining: map has 10000 buckets, each starting with a dummy HashMapNode(0, 0)
    sentinel. Every operation walks the chain checking curr.next (never curr itself), so
    removing the first real entry needs no special case - it's the same splice as any
    other node.

    Resize / load factor: never resizes here - 10000 buckets already covers the problem's
    max number of keys. A dynamic version would resize past load factor (entries / buckets)
    > 0.75, Java's HashMap default.
    """

    def __init__(self):
        """
        Complexity:
            Time complexity: O(b); where b is the number of buckets (10000) - one dummy
                node is created per bucket
            Space complexity: O(b); one dummy node stored per bucket
        """
        # T | S
        self.map = [HashMapNode(0, 0) for _ in range(10000)]  # O(b) | O(b)

    def hash(self, key):
        """
        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        return key % len(self.map)  # O(1) | O(1)

    def put(self, key: int, value: int) -> None:
        """
        1. Get curr = map[hash(key)] (the bucket's dummy head)
        2. While curr.next:
            2.1 If curr.next.key == key: update curr.next.val and return (key already exists)
            2.2 Otherwise: advance curr = curr.next
        3. Set curr.next = HashMapNode(key, value) (append a new node at the end of the chain)

        Complexity:
            Time complexity: O(n); where n is the number of nodes in the bucket
            Space complexity: O(1)
        """
        # T | S
        curr = self.map[self.hash(key)]  # O(1) | O(1)

        while curr.next:  # O(n) | O(1)
            if curr.next.key == key:  # O(1) | O(1)
                curr.next.val = value  # O(1) | O(1)
                return  # O(1) | O(1)
            curr = curr.next  # O(1) | O(1)

        curr.next = HashMapNode(key, value)  # O(1) | O(1)

    def get(self, key: int) -> int:
        """
        1. Get curr = map[hash(key)] (the bucket's dummy head)
        2. While curr.next:
            2.1 If curr.next.key == key: return curr.next.val
            2.2 Otherwise: advance curr = curr.next
        3. return -1 (key not found in this bucket)

        Complexity:
            Time complexity: O(n); where n is the number of nodes in the bucket
            Space complexity: O(1)
        """
        # T | S
        curr = self.map[self.hash(key)]  # O(1) | O(1)

        while curr.next:  # O(n) | O(1)
            if curr.next.key == key:  # O(1) | O(1)
                return curr.next.val  # O(1) | O(1)
            curr = curr.next  # O(1) | O(1)

        return -1  # O(1) | O(1)

    def remove(self, key: int) -> None:
        """
        1. Get curr = map[hash(key)] (the bucket's dummy head)
        2. While curr.next:
            2.1 If curr.next.key == key: set curr.next = curr.next.next (skip the target
                node, since curr is always the node right before the one we're checking -
                there's never a special case for "the key is the first real node")
            2.2 Otherwise: advance curr = curr.next

        Complexity:
            Time complexity: O(n); where n is the number of nodes in the bucket
            Space complexity: O(1)
        """
        # T | S
        curr = self.map[self.hash(key)]  # O(1) | O(1)

        while curr.next:  # O(n) | O(1)
            if curr.next.key == key:  # O(1) | O(1)
                curr.next = curr.next.next  # O(1) | O(1)
                return  # O(1) | O(1)
            curr = curr.next  # O(1) | O(1)


def detectCycle(head: ListNode | None) -> ListNode | None:
    """
    Example: head = [3,2,0,-4] with the tail pointing back to node "2" (cycle entry = node "2")

    1. Define slow = head, fast = head
    2. While fast and fast.next:
        2.1 Set slow = slow.next, fast = fast.next.next
        2.2 If slow == fast: they met inside the cycle
            2.2.1 Reset fast = head
            2.2.2 While fast != slow: advance both fast and slow one node at a time
            2.2.3 return fast (now sitting at the cycle's entry point)
    3. return None (fast reached the end, so there's no cycle)

    Complexity:
        Time complexity: O(n); where n is the number of nodes in the list - Floyd's
            detection phase and the entry-finding phase each take at most O(n)
        Space complexity: O(1); only a constant number of pointers are used
    """
    # T | S
    slow = head  # O(1) | O(1)
    fast = head  # O(1) | O(1)

    while fast and fast.next:  # O(n) | O(1)
        slow = slow.next  # O(1) | O(1)
        fast = fast.next.next  # O(1) | O(1)

        if slow == fast:  # O(1) | O(1)
            fast = head  # O(1) | O(1)

            while fast != slow:  # O(n) | O(1)
                fast = fast.next  # O(1) | O(1)
                slow = slow.next  # O(1) | O(1)

            return fast  # O(1) | O(1)

    return None  # O(1) | O(1)
