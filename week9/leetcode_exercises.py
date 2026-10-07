from collections import deque


def numIslands(grid: list[list[str]]) -> int:
    """
    Example: grid = [["1","1","0","0","0"],
                     ["1","1","0","0","0"],
                     ["0","0","1","0","0"],
                     ["0","0","0","1","1"]]

    1. Define rows = len(grid), cols = len(grid[0])
    2. Define islands = 0
    3. Define directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    4. For every cell (row, col):
        4.1 If grid[row][col] == "1": a new island starts here
            4.1.1 Increment islands
            4.1.2 Sink the cell (set it to "0") and enqueue it
            4.1.3 While queue:
                - Popleft (current_row, current_col)
                - For each neighbour inside the grid that is "1": sink it and enqueue it
                    (sinking when enqueuing avoids adding the same cell twice)
    5. return islands

    Complexity:
        Time complexity: O(m * n); where m and n are the number of rows and columns -
            every cell is sunk and enqueued at most once
        Space complexity: O(m * n); the queue in the worst case (grid full of land)
    """
    # T | S
    rows = len(grid)  # O(1) | O(1)
    cols = len(grid[0])  # O(1) | O(1)
    islands = 0  # O(1) | O(1)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # O(1) | O(1)

    for row in range(rows):  # O(m) | O(1)
        for col in range(cols):  # O(n) | O(1)
            if grid[row][col] == "1":  # O(1) | O(1)
                islands += 1  # O(1) | O(1)
                grid[row][col] = "0"  # O(1) | O(1)
                queue = deque([(row, col)])  # O(1) | O(1)

                while queue:  # O(m * n) total | O(m * n)
                    current_row, current_col = queue.popleft()  # O(1) | O(1)

                    for dr, dc in directions:  # O(1) | O(1)
                        next_row = current_row + dr  # O(1) | O(1)
                        next_col = current_col + dc  # O(1) | O(1)

                        if (
                            0 <= next_row < rows
                            and 0 <= next_col < cols
                            and grid[next_row][next_col] == "1"
                        ):  # O(1) | O(1)
                            grid[next_row][next_col] = "0"  # O(1) | O(1)
                            queue.append((next_row, next_col))  # O(1) | O(1)

    return islands  # O(1) | O(1)


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Example: numCourses = 2, prerequisites = [[1,0],[0,1]] (cycle, so it's impossible)

    1. Define graph = [[] for each course] (course b -> courses that need b first)
    2. Define in_degree = [0] * numCourses (how many prerequisites each course is missing)
    3. For course, prerequisite in prerequisites:
        3.1 Append course to graph[prerequisite]
        3.2 Increment in_degree[course]
    4. Define queue = deque with every course whose in_degree is 0 (can be taken right now)
    5. Define taken = 0
    6. While queue (Kahn's algorithm):
        6.1 Popleft course and increment taken
        6.2 For next_course in graph[course]:
            6.2.1 Decrement in_degree[next_course] (one prerequisite is done)
            6.2.2 If in_degree[next_course] == 0: enqueue next_course
    7. return taken == numCourses (courses inside a cycle never reach in_degree 0)

    Complexity:
        Time complexity: O(V + E); where V is numCourses and E is the number of prerequisites
        Space complexity: O(V + E); for the adjacency list, in_degree and the queue
    """
    # T | S
    graph = [[] for _ in range(numCourses)]  # O(V) | O(V)
    in_degree = [0] * numCourses  # O(V) | O(V)

    for course, prerequisite in prerequisites:  # O(E) | O(E)
        graph[prerequisite].append(course)  # O(1) | O(1)
        in_degree[course] += 1  # O(1) | O(1)

    queue = deque(course for course in range(numCourses) if in_degree[course] == 0)  # O(V) | O(V)
    taken = 0  # O(1) | O(1)

    while queue:  # O(V) | O(1)
        course = queue.popleft()  # O(1) | O(1)
        taken += 1  # O(1) | O(1)

        for next_course in graph[course]:  # O(E) total | O(1)
            in_degree[next_course] -= 1  # O(1) | O(1)

            if in_degree[next_course] == 0:  # O(1) | O(1)
                queue.append(next_course)  # O(1) | O(1)

    return taken == numCourses  # O(1) | O(1)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node: Node | None) -> Node | None:
    """
    Example: adjList = [[2,4],[1,3],[2,4],[1,3]]

    1. Define clones = {} (original node -> its clone; also works as the visited set)
    2. Define clone(original):
        2.1 If original in clones: return clones[original] (already copied, avoids
            infinite loops on cycles)
        2.2 Define copy = Node(original.val)
        2.3 Set clones[original] = copy (register it BEFORE visiting neighbours)
        2.4 For neighbor in original.neighbors: append clone(neighbor) to copy.neighbors
        2.5 return copy
    3. return clone(node) if node else None

    Complexity:
        Time complexity: O(V + E); where V is the number of nodes and E the number of edges
        Space complexity: O(V); for clones and the recursion call stack
    """
    # T | S
    clones = {}  # O(1) | O(1)

    def clone(original: Node) -> Node:
        if original in clones:  # O(1) | O(1)
            return clones[original]  # O(1) | O(1)

        copy = Node(original.val)  # O(1) | O(1)
        clones[original] = copy  # O(1) | O(1)

        for neighbor in original.neighbors:  # O(E) total | O(V)
            copy.neighbors.append(clone(neighbor))  # O(1) | O(1)

        return copy  # O(1) | O(1)

    return clone(node) if node else None  # O(V + E) | O(V)


def findCircleNum(isConnected: list[list[int]]) -> int:
    """
    Example: isConnected = [[1,1,0],[1,1,0],[0,0,1]]

    1. Define n = len(isConnected)
    2. Define parent = list(range(n)) (every city starts as its own root)
    3. Define provinces = n
    4. Define find(x):
        4.1 If parent[x] != x: set parent[x] = find(parent[x]) (path compression: point x
            straight to the root)
        4.2 return parent[x]
    5. For i in range(n):
        5.1 For j in range(i + 1, n) (the matrix is symmetric, so only the upper half):
            5.1.1 If isConnected[i][j] == 1:
                - Get root_i = find(i), root_j = find(j)
                - If root_i != root_j: set parent[root_j] = root_i and decrement provinces
                    (two different provinces were merged into one)
    6. return provinces

    Complexity:
        Time complexity: O(n² log n); where n is the number of cities - n² pairs, and each
            find is O(log n) amortized with path compression
        Space complexity: O(n); for parent and the find recursion call stack
    """
    # T | S
    n = len(isConnected)  # O(1) | O(1)
    parent = list(range(n))  # O(n) | O(n)
    provinces = n  # O(1) | O(1)

    def find(x: int) -> int:
        if parent[x] != x:  # O(1) | O(1)
            parent[x] = find(parent[x])  # O(log n) | O(n)

        return parent[x]  # O(1) | O(1)

    for i in range(n):  # O(n) | O(1)
        for j in range(i + 1, n):  # O(n) | O(1)
            if isConnected[i][j] == 1:  # O(1) | O(1)
                root_i = find(i)  # O(log n) | O(n)
                root_j = find(j)  # O(log n) | O(n)

                if root_i != root_j:  # O(1) | O(1)
                    parent[root_j] = root_i  # O(1) | O(1)
                    provinces -= 1  # O(1) | O(1)

    return provinces  # O(1) | O(1)


def orangesRotting(grid: list[list[int]]) -> int:
    """
    Example: grid = [[2,1,1],[1,1,0],[0,1,1]]

    1. Define rows = len(grid), cols = len(grid[0])
    2. Define queue = deque(), fresh = 0
    3. For every cell (row, col):
        3.1 If grid[row][col] == 2: enqueue (row, col) (multi-source BFS: all rotten
            oranges start at the same time)
        3.2 If grid[row][col] == 1: increment fresh
    4. Define minutes = 0
    5. Define directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    6. While queue and fresh > 0:
        6.1 Increment minutes (each BFS level is one minute)
        6.2 For _ in range(len(queue)) (only the oranges that were rotten at this minute):
            6.2.1 Popleft (row, col)
            6.2.2 For each neighbour inside the grid that is 1: set it to 2, decrement
                fresh and enqueue it
    7. return minutes if fresh == 0 else -1 (some fresh orange was never reached)

    Complexity:
        Time complexity: O(m * n); where m and n are the number of rows and columns -
            every cell is enqueued at most once
        Space complexity: O(m * n); for the queue
    """
    # T | S
    rows = len(grid)  # O(1) | O(1)
    cols = len(grid[0])  # O(1) | O(1)
    queue = deque()  # O(1) | O(1)
    fresh = 0  # O(1) | O(1)

    for row in range(rows):  # O(m) | O(1)
        for col in range(cols):  # O(n) | O(1)
            if grid[row][col] == 2:  # O(1) | O(1)
                queue.append((row, col))  # O(1) | O(m * n)
            elif grid[row][col] == 1:  # O(1) | O(1)
                fresh += 1  # O(1) | O(1)

    minutes = 0  # O(1) | O(1)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # O(1) | O(1)

    while queue and fresh > 0:  # O(m * n) | O(m * n)
        minutes += 1  # O(1) | O(1)

        for _ in range(len(queue)):  # O(size of the level) | O(1)
            row, col = queue.popleft()  # O(1) | O(1)

            for dr, dc in directions:  # O(1) | O(1)
                next_row = row + dr  # O(1) | O(1)
                next_col = col + dc  # O(1) | O(1)

                if (
                    0 <= next_row < rows
                    and 0 <= next_col < cols
                    and grid[next_row][next_col] == 1
                ):  # O(1) | O(1)
                    grid[next_row][next_col] = 2  # O(1) | O(1)
                    fresh -= 1  # O(1) | O(1)
                    queue.append((next_row, next_col))  # O(1) | O(1)

    return minutes if fresh == 0 else -1  # O(1) | O(1)
