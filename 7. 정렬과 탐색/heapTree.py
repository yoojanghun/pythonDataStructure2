# 힙 트리
# 최대 힙(max heap): 부모 노드 키 값이 자식 노드의 키 값보다 크거나 같은 완전이진트리
# 최소 힙(min heap): 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전이진트리
N = 20

class MaxHeap:                          # 부모가 더 크다
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0               # 가장 마지막 노드의 위치 번호(= 노드 수)

    def upHeap(self):                   # insert할 때 사용
        i = self.heapSize               # i = 마지막 노드 index
        key = self.heap[i]              # key = 마지막 노드의 값

        while(i != 1) and (key > self.heap[i // 2]):        # i가 가장 처음이 아니고, key가 부모보다 더 클 때
            self.heap[i] = self.heap[i // 2]                # 부모를 자식에 덮어씌움
            i = i // 2
        self.heap[i] = key              # 최종 i 위치에 key값을 대입

    def insertItem(self, item):
        self.heapSize += 1
        self.heap[self.heapSize] = item
        self.upHeap()

    def downHeap(self):                 # delete할 때 사용, 자식 노드 2개 중 더 큰 것과 key랑 비교
        parent = 1
        child = 2
        key = self.heap[parent]

        while child <= self.heapSize:   # 더 내려갈 자식이 있을 때까지
            if (child < self.heapSize) and (self.heap[child + 1] > self.heap[child]):
                child += 1              # 오른쪽 자식이 더 크면, 오른쪽 자식과 key랑 비교

            if key >= self.heap[child]:
                break

            self.heap[parent] = self.heap[child]        # break 안 걸리면 자식이 key보다 더 큰 것
            parent = child
            child *= 2

        self.heap[parent] = key

    # 가장 높은 노드를 마지막 노드로 대체, 그 후, 마지막 노드 삭제
    def deleteItem(self):
        key = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1
        self.downHeap()

        return key                      # 결국엔 가장 위에 있는 노드를 삭제한 것임.

if __name__ == "__main__":
    H = MaxHeap()
    data = [9, 7, 6, 5, 4, 3, 2, 2, 1, 3]

    for n in data:
        H.insertItem(n)
        print("Heap :", H.heap[1:H.heapSize + 1])

    H.insertItem(8)
    print("Heap :", H.heap[1:H.heapSize + 1])
    print()

    print("[%d] is deleted" % H.deleteItem())
    print("Heap :", H.heap[1:H.heapSize + 1])