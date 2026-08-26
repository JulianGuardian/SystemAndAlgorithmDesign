def subsets(nums: list[int]) -> list[list[int]]:
    """Power set. Time O(n·2ⁿ), Space O(n·2ⁿ)."""
    results = []

    def backtrack(start: int, current: list[int]):
        results.append(list(current))  # every node is a valid subset
        for i in range(start, len(nums)):
            current.append(nums[i])  # CHOOSE
            backtrack(i + 1, current)  # EXPLORE (only elements after i)
            current.pop()  # UNCHOOSE

    backtrack(0, [])
    return results


print(subsets([1, 2, 3]))
"""
Prueba de escritorio (nums=[1,2,3], results=[]):
# Paso | Nivel |  i  | Llamada activa          | Instrucción                     | current    | results
# -----|-------|-----|-------------------------|---------------------------------|------------|--------------------------------------
#   1  |  0    |  -  | backtrack(0, [])        | results.append([])              | []         | [[]]
#   2  |  0    |  0  |                         | i=0: current.append(1)          | [1]        | [[]]
#   3  |  1    |  -  | backtrack(1, [1])       | results.append([1])             | [1]        | [[], [1]]
#   4  |  1    |  1  |                         | i=1: current.append(2)          | [1,2]      | [[], [1]]
#   5  |  2    |  -  | backtrack(2, [1,2])     | results.append([1,2])           | [1,2]      | [[], [1], [1,2]]
#   6  |  2    |  2  |                         | i=2: current.append(3)          | [1,2,3]    | [[], [1], [1,2]]
#   7  |  3    |  -  | backtrack(3, [1,2,3])   | results.append([1,2,3])         | [1,2,3]    | [[], [1], [1,2], [1,2,3]]
#   8  |  3    |  -  |                         | range(3,3) vacío -> retorna     | [1,2,3]    | [[], [1], [1,2], [1,2,3]]
#   9  |  2    |  2  | backtrack(2, [1,2])     | current.pop() (quita 3)         | [1,2]      | [[], [1], [1,2], [1,2,3]]
#  10  |  2    |  2  |                         | fin for (i=2) -> retorna        | [1,2]      | [[], [1], [1,2], [1,2,3]]
#  11  |  1    |  1  | backtrack(1, [1])       | current.pop() (quita 2)         | [1]        | [[], [1], [1,2], [1,2,3]]
#  12  |  1    |  2  |                         | i=2: current.append(3)          | [1,3]      | [[], [1], [1,2], [1,2,3]]
#  13  |  2    |  -  | backtrack(3, [1,3])     | results.append([1,3])           | [1,3]      | [[], [1], [1,2], [1,2,3], [1,3]]
#  14  |  2    |  -  |                         | range(3,3) vacío -> retorna     | [1,3]      | [[], [1], [1,2], [1,2,3], [1,3]]
#  15  |  1    |  2  | backtrack(1, [1])       | current.pop() (quita 3)         | [1]        | [[], [1], [1,2], [1,2,3], [1,3]]
#  16  |  1    |  2  |                         | fin for (i=2) -> retorna        | [1]        | [[], [1], [1,2], [1,2,3], [1,3]]
#  17  |  0    |  0  | backtrack(0, [])        | current.pop() (quita 1)         | []         | [[], [1], [1,2], [1,2,3], [1,3]]
#  18  |  0    |  1  |                         | i=1: current.append(2)          | [2]        | [[], [1], [1,2], [1,2,3], [1,3]]
#  19  |  1    |  -  | backtrack(2, [2])       | results.append([2])             | [2]        | [[], [1], [1,2], [1,2,3], [1,3], [2]]
#  20  |  1    |  2  |                         | i=2: current.append(3)          | [2,3]      | [[], [1], [1,2], [1,2,3], [1,3], [2]]
#  21  |  2    |  -  | backtrack(3, [2,3])     | results.append([2,3])           | [2,3]      | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  22  |  2    |  -  |                         | range(3,3) vacío -> retorna     | [2,3]      | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  23  |  1    |  2  | backtrack(2, [2])       | current.pop() (quita 3)         | [2]        | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  24  |  1    |  2  |                         | fin for (i=2) -> retorna        | [2]        | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  25  |  0    |  1  | backtrack(0, [])        | current.pop() (quita 2)         | []         | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  26  |  0    |  2  |                         | i=2: current.append(3)          | [3]        | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3]]
#  27  |  1    |  -  | backtrack(3, [3])       | results.append([3])             | [3]        | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
#  28  |  1    |  -  |                         | range(3,3) vacío -> retorna     | [3]        | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
#  29  |  0    |  2  | backtrack(0, [])        | current.pop() (quita 3)         | []         | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
#  30  |  0    |  2  |                         | fin for (i=2) -> retorna        | []         | [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
# Resultado final: [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
"""
