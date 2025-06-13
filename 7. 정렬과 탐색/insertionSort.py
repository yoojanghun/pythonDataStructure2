# 삽입 정렬
# 왼손에 정렬된 카드. 오른손에 추가로 받은 카드. 오른손의 카드를 왼손의 정렬된 카드에 끼워 넣음.
# 정렬이 안 된 부분의 숫자를 하나씩 정렬된 부분의 적절한 위치를 찾아 끼워 넣는 과정 반복.

def printStep(A, idx):
    print("   Step %d : " %idx, end="")
    print(A)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key

        printStep(A, i)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Before    :", data)

    insertionSort(data)

    print("Selection :", data)
    print()

# 시간 복잡도
# 최선의 경우 O(n): 이미 정렬되어 있는 경우엔 비교 n-1번
# 최악의 경우 O(n^2): 역순으로 정렬되어 있는 경우
# 평균의 경우 O(n^2)

# 많은 이동 필요 => 레코드가 큰 경우 불리
# 안정성 o