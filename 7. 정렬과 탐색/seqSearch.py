# 순차 탐색
# 정렬되지 않은 배열에 적용 가능
# 배열을 처음부터 마지막까지 하나씩 검사
# 평균 비교 횟수: (n+1)/2번 비교 (최악의 경우 n번)
# 찾고 싶은 대상을 key라고 함.
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

def seqSearch(A, key):
    n = len(A)

    for i in range(n):
        if A[i] == key:
            return i            # 인덱스 return

    return -1

if __name__ == "__main__":
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))

    insertionSort(A)
    print("A =", A)

    key = int(input("Input Search Key : "))

    idx = seqSearch(A, key)

    if idx != -1:
        print("%d 위치에서 발견" % idx)
    else:
        print("키가 존재하지 않습니다.")

# 시간 복잡도: O(n)