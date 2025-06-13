# 이진 탐색(반복 구조)
# 정렬된 배열의 탐색에 적합
# 배열의 중앙에 있는 값을 조사하여, 찾고자 하는 항목이 왼쪽 또는 오른쪽 부분에 있는 지 확인.
# 이 과정 반복하여 탐색의 범위를 반으로 줄여가며 탐색 진행
import random

def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = key

def iBinarySearch(A, key):
    low = 0
    high = len(A) - 1

    while(low <= high):
        mid = (low + high) // 2
        print("방문한 원소:", A[mid], end=" ")

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

if __name__ == "__main__":
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))

    insertionSort(A)
    print("A =", A)

    key = int(input("Input Search Key : "))

    idx = iBinarySearch(A, key)

    print()

    if idx != -1:
        print("%d 위치에서 발견" % idx)
    else:
        print("키가 존재하지 않습니다.")