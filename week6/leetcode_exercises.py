from collections import deque


def isValid(s: str) -> bool:
    """
    Example: s = "([)]"

    1. If s is empty: return True (nothing to match)
    2. If len(s) is odd: return False (brackets come in pairs, so one can't be matched)
    3. Define stack = []
    4. Define matching = {")": "(", "]": "[", "}": "{"} (closing -> expected opening)
    5. For char in s:
        5.1 If char is a closing bracket:
            5.1.1 If stack is empty or stack[-1] != matching[char]: return False
                (nothing to close, or the most recent opening is the wrong type)
            5.1.2 Pop the matched opening from stack
        5.2 Otherwise: push char to stack (it's an opening bracket)
    6. return len(stack) == 0 (every opening must have been closed)

    Complexity:
        Time complexity: O(n); where n is the length of s
        Space complexity: O(n); the stack can hold up to n opening brackets
    """
    # T | S
    if not s:  # O(1) | O(1)
        return True  # O(1) | O(1)

    if len(s) % 2 == 1:  # O(1) | O(1)
        return False  # O(1) | O(1)

    stack = []  # O(1) | O(1)
    matching = {")": "(", "]": "[", "}": "{"}  # O(1) | O(1)

    for char in s:  # O(n) | O(n)
        if char in matching:  # O(1) | O(1)
            if not stack or stack[-1] != matching[char]:  # O(1) | O(1)
                return False  # O(1) | O(1)
            stack.pop()  # O(1) | O(1)
        else:
            stack.append(char)  # O(1) | O(1)

    return len(stack) == 0  # O(1) | O(1)


class MinStack:
    """
    Auxiliary stack: min_stack[i] stores the minimum of stack[0..i], so both stacks always
    have the same size and the current minimum is always min_stack[-1]. Popping both
    stacks together restores the previous minimum automatically - no rescan needed.
    """

    def __init__(self):
        """
        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        self.stack = []  # O(1) | O(1)
        self.min_stack = []  # O(1) | O(1)

    def push(self, val: int) -> None:
        """
        1. Push val to stack
        2. If min_stack is empty: push val to min_stack
        3. Otherwise: push min(val, min_stack[-1]) to min_stack

        Complexity:
            Time complexity: O(1)
            Space complexity: O(1) per call; O(n) overall for n pushed values
        """
        # T | S
        self.stack.append(val)  # O(1) | O(1)

        if not self.min_stack:  # O(1) | O(1)
            self.min_stack.append(val)  # O(1) | O(1)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))  # O(1) | O(1)

    def pop(self) -> None:
        """
        1. Pop from stack and min_stack together (keeps them the same size)

        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        self.stack.pop()  # O(1) | O(1)
        self.min_stack.pop()  # O(1) | O(1)

    def top(self) -> int:
        """
        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        return self.stack[-1]  # O(1) | O(1)

    def getMin(self) -> int:
        """
        Complexity:
            Time complexity: O(1)
            Space complexity: O(1)
        """
        # T | S
        return self.min_stack[-1]  # O(1) | O(1)


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Example: temperatures = [73,74,75,71,69,72,76,73]

    1. Define result = [0] * len(temperatures)
    2. Define stack = [] (indices of days still waiting for a warmer day; their
        temperatures are kept in decreasing order)
    3. For index, temperature in enumerate(temperatures):
        3.1 While stack and temperature > temperatures[stack[-1]]:
            3.1.1 Pop previous_index from stack (today is its first warmer day)
            3.1.2 Set result[previous_index] = index - previous_index
        3.2 Push index to stack
    4. return result (indices left in the stack never found a warmer day, so they stay 0)

    Complexity:
        Time complexity: O(n); where n is the length of temperatures - each index is
            pushed once and popped at most once, so the inner while is amortized O(1)
        Space complexity: O(n); for result and the stack
    """
    # T | S
    result = [0] * len(temperatures)  # O(n) | O(n)
    stack = []  # O(1) | O(1)

    for index, temperature in enumerate(temperatures):  # O(n) | O(n)
        while stack and temperature > temperatures[stack[-1]]:  # O(1) amortized | O(1)
            previous_index = stack.pop()  # O(1) | O(1)
            result[previous_index] = index - previous_index  # O(1) | O(1)

        stack.append(index)  # O(1) | O(1)

    return result  # O(1) | O(1)


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Example: nums = [1,3,-1,-3,5,3,6,7], k = 3

    1. Define result = []
    2. Define window = deque() (indices whose values are in decreasing order, so
        window[0] is always the index of the current window's maximum)
    3. For index, number in enumerate(nums):
        3.1 If window and window[0] <= index - k: popleft (front index slid out of the window)
        3.2 While window and nums[window[-1]] < number: pop from the back (those values
            are older AND smaller, so they can never be a window maximum again)
        3.3 Append index to window
        3.4 If index >= k - 1: append nums[window[0]] to result (the first full window is ready)
    4. return result

    Complexity:
        Time complexity: O(n); where n is the length of nums - each index is appended
            once and removed at most once
        Space complexity: O(k); the deque never holds more than k indices (result
            excluded, since it's the output)
    """
    # T | S
    result = []  # O(1) | O(1)
    window = deque()  # O(1) | O(1)

    for index, number in enumerate(nums):  # O(n) | O(k)
        if window and window[0] <= index - k:  # O(1) | O(1)
            window.popleft()  # O(1) | O(1)

        while window and nums[window[-1]] < number:  # O(1) amortized | O(1)
            window.pop()  # O(1) | O(1)

        window.append(index)  # O(1) | O(1)

        if index >= k - 1:  # O(1) | O(1)
            result.append(nums[window[0]])  # O(1) | O(1)

    return result  # O(1) | O(1)


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    """
    Example: mat = [[0,0,0],[0,1,0],[1,1,1]]

    1. Define rows = len(mat), cols = len(mat[0])
    2. Define distances = rows x cols grid filled with infinity
    3. Define queue = deque()
    4. For every cell (row, col):
        4.1 If mat[row][col] == 0: set distances[row][col] = 0 and enqueue (row, col)
            (multi-source BFS: all zeros start at the same time)
    5. Define directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    6. While queue:
        6.1 Popleft (row, col)
        6.2 For each (dr, dc) in directions:
            6.2.1 Get next_row = row + dr, next_col = col + dc
            6.2.2 If (next_row, next_col) is inside the grid and
                distances[next_row][next_col] > distances[row][col] + 1:
                - Set distances[next_row][next_col] = distances[row][col] + 1
                - Enqueue (next_row, next_col)
                (BFS reaches each cell first from its nearest zero, so it's set only once)
    7. return distances

    Complexity:
        Time complexity: O(m * n); where m and n are the number of rows and columns -
            every cell is enqueued once and checks 4 neighbors
        Space complexity: O(m * n); for distances and the queue
    """
    # T | S
    rows = len(mat)  # O(1) | O(1)
    cols = len(mat[0])  # O(1) | O(1)
    distances = [[float("inf")] * cols for _ in range(rows)]  # O(m * n) | O(m * n)
    queue = deque()  # O(1) | O(1)

    for row in range(rows):  # O(m) | O(1)
        for col in range(cols):  # O(n) | O(1)
            if mat[row][col] == 0:  # O(1) | O(1)
                distances[row][col] = 0  # O(1) | O(1)
                queue.append((row, col))  # O(1) | O(m * n)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # O(1) | O(1)

    while queue:  # O(m * n) | O(m * n)
        row, col = queue.popleft()  # O(1) | O(1)

        for dr, dc in directions:  # O(1) | O(1)
            next_row = row + dr  # O(1) | O(1)
            next_col = col + dc  # O(1) | O(1)

            if (
                0 <= next_row < rows
                and 0 <= next_col < cols
                and distances[next_row][next_col] > distances[row][col] + 1
            ):  # O(1) | O(1)
                distances[next_row][next_col] = distances[row][col] + 1  # O(1) | O(1)
                queue.append((next_row, next_col))  # O(1) | O(1)

    return distances  # O(1) | O(1)
