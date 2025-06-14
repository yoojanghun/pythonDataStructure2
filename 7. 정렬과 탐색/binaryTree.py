# 순회
# 트리에 속하는 모든 노드를 한 번씩 방문하는 것. 트리의 모든 노드들을 화면에 출력하기 위해서 순회가 필요.
# 전위 순회(preOrder traversal): 루트 노드 - 왼쪽 아래 - 오른쪽 아래 순서로 순회
# 중위 순회(inOrder traversal): 왼쪽 아래 - 루트 노드 - 오른쪽 아래 순서로 순회
# 후위 순회(postOrder traversal): 왼쪽 아래 - 오른쪽 아래 - 루트 노드 순서로 순회
import queue

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data        # 루트 노드
        self.left = left        # 왼쪽 아래 루트 노드
        self.right = right      # 오른쪽 아래 루트 노드

class BinaryTree:
    def __init__(self):
        self.root = None

    def preOrder(self, root):
        if root != None:
            print("[%c] " % root.data, end="")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root != None:
            self.inOrder(root.left)
            print("[%c] " % root.data, end="")
            self.inOrder(root.right)

    def postOrder(self, root):
        if root != None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print("[%c] " % root.data, end="")

if __name__ == "__main__":
    T = BinaryTree()

    N6 = Node("F")
    N5 = Node("E")
    N4 = Node("D")
    N3 = Node("C", N6, None)
    N2 = Node("B", N4, N5)
    N1 = Node("A", N2, N3)

    print("Pre  : ", end="");   T.preOrder(N1);     print()
    print("In   : ", end="");   T.inOrder(N1);      print()
    print("Post : ", end="");   T.postOrder(N1);    print()