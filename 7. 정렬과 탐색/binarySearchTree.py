# 이진 탐색 트리
# 루트노드 왼쪽 서브트리에 있는 값들은 루트노드보다 작다
# 루트노드 오른쪽 서브트리에 있는 값들은 루트노드보다 크다
# 이러한 성질은 모든 노드에서 만족되어야 한다.

# insert연산을 통해 새로운 노드 n이 저장되어야 하는 트리상의 위치는 단 하나뿐이다.
# 삭제연산을 할 때, 이진탐색트리의 조건을 유지하는 형태로 트리가 재구성되어야 한다.
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def preOrder(root):
    if root != None:
        print("%2d " % root.key, end="")
        preOrder(root.left)
        preOrder(root.right)

def insert(root, key):
    if root == None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        pass

    return root

def getMinNode(root):
    while root != None and root.left != None:
        root = root.left

    return root


