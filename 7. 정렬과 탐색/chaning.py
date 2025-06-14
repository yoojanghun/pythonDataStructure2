# 체이닝: 하나의 버킷에 여러 레코드를 저장할 수 있도록 하는 방법(연결 리스트 사용)
M = 13

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class HashTable:
    def __init__(self):
        self.table = [None] * M

    def hashFn(self, key):
        return key % M

    def insert(self, key):
        bucket = self.hashFn(key)
        node = Node(key)
        node.next = self.table[bucket]      # self.table[bucket]은 버킷에 저장된 연결 리스트의 맨 앞 노드
        self.table[bucket] = node           # 맨 앞 노드(self.table[bucket])을 node로 한다.

    def display(self):
        for i in range(M):
            print("HT[%02d] : " % i, end="")
            n = self.table[i]

            while n is not None:
                print(n.data, end=" ")
                n = n.next
            print()

if __name__ == "__main__":
    import random
    HT = HashTable()

    for i in range(20):
        HT.insert(random.randint(10, 99))

    HT.display()