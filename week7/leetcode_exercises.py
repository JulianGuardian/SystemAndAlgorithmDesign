class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: TreeNode | None) -> int:
    """
    Example: root = [3,9,20,null,null,15,7]

    1. If root is None: return 0 (base case, an empty tree has depth 0)
    2. Get left_depth = maxDepth(root.left)
    3. Get right_depth = maxDepth(root.right)
    4. return 1 + max(left_depth, right_depth) (count the current node plus the deeper side)

    Complexity:
        Time complexity: O(n); where n is the number of nodes - each node is visited once
        Space complexity: O(h); where h is the height of the tree (recursion call stack) -
            O(log n) if balanced, O(n) if completely skewed
    """
    # T | S
    if not root:  # O(1) | O(1)
        return 0  # O(1) | O(1)

    left_depth = maxDepth(root.left)  # O(n) | O(h)
    right_depth = maxDepth(root.right)  # O(n) | O(h)

    return 1 + max(left_depth, right_depth)  # O(1) | O(1)


def diameterOfBinaryTree(root: TreeNode | None) -> int:
    """
    Example: root = [1,2,3,4,5]

    1. Define diameter = 0
    2. Define height(node):
        2.1 If node is None: return 0
        2.2 Get left_height = height(node.left)
        2.3 Get right_height = height(node.right)
        2.4 Set diameter = max(diameter, left_height + right_height) (longest path that
            passes through this node, measured in edges)
        2.5 return 1 + max(left_height, right_height)
    3. Call height(root)
    4. return diameter

    Complexity:
        Time complexity: O(n); where n is the number of nodes - each node is visited once
        Space complexity: O(h); where h is the height of the tree (recursion call stack)
    """
    # T | S
    diameter = 0  # O(1) | O(1)

    def height(node: TreeNode | None) -> int:
        nonlocal diameter

        if not node:  # O(1) | O(1)
            return 0  # O(1) | O(1)

        left_height = height(node.left)  # O(n) | O(h)
        right_height = height(node.right)  # O(n) | O(h)

        diameter = max(diameter, left_height + right_height)  # O(1) | O(1)

        return 1 + max(left_height, right_height)  # O(1) | O(1)

    height(root)  # O(n) | O(h)
    return diameter  # O(1) | O(1)


def lowestCommonAncestorBST(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Example: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

    1. Define current = root
    2. While current:
        2.1 If p.val < current.val and q.val < current.val: set current = current.left
            (both nodes are in the left subtree)
        2.2 Else if p.val > current.val and q.val > current.val: set current = current.right
            (both nodes are in the right subtree)
        2.3 Otherwise: return current (p and q split here, or one of them is current)

    Complexity:
        Time complexity: O(h); where h is the height of the tree - one node per level
        Space complexity: O(1); iterative, only one pointer is used
    """
    # T | S
    current = root  # O(1) | O(1)

    while current:  # O(h) | O(1)
        if p.val < current.val and q.val < current.val:  # O(1) | O(1)
            current = current.left  # O(1) | O(1)
        elif p.val > current.val and q.val > current.val:  # O(1) | O(1)
            current = current.right  # O(1) | O(1)
        else:
            return current  # O(1) | O(1)


def lowestCommonAncestor(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    Example: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

    1. If root is None or root == p or root == q: return root (base case)
    2. Get left = lowestCommonAncestor(root.left, p, q)
    3. Get right = lowestCommonAncestor(root.right, p, q)
    4. If left and right: return root (p and q were found on different sides)
    5. return left if left else right (pass up whichever side found something)

    Complexity:
        Time complexity: O(n); where n is the number of nodes - each node is visited once
        Space complexity: O(h); where h is the height of the tree (recursion call stack)
    """
    # T | S
    if not root or root == p or root == q:  # O(1) | O(1)
        return root  # O(1) | O(1)

    left = lowestCommonAncestor(root.left, p, q)  # O(n) | O(h)
    right = lowestCommonAncestor(root.right, p, q)  # O(n) | O(h)

    if left and right:  # O(1) | O(1)
        return root  # O(1) | O(1)

    return left if left else right  # O(1) | O(1)


def isValidBST(root: TreeNode | None) -> bool:
    """
    Example: root = [5,1,4,null,null,3,6]

    1. Define check(node, low, high):
        1.1 If node is None: return True (an empty tree is a valid BST)
        1.2 If not (low < node.val < high): return False (node breaks an ancestor's bound,
            not only its parent's)
        1.3 return check(node.left, low, node.val) and check(node.right, node.val, high)
            (left subtree must be smaller than node, right subtree must be greater)
    2. return check(root, -infinity, infinity)

    Complexity:
        Time complexity: O(n); where n is the number of nodes - each node is visited once
        Space complexity: O(h); where h is the height of the tree (recursion call stack)
    """

    # T | S
    def check(node: TreeNode | None, low: float, high: float) -> bool:
        if not node:  # O(1) | O(1)
            return True  # O(1) | O(1)

        if not (low < node.val < high):  # O(1) | O(1)
            return False  # O(1) | O(1)

        return check(node.left, low, node.val) and check(node.right, node.val, high)  # O(n) | O(h)

    return check(root, float("-inf"), float("inf"))  # O(n) | O(h)
