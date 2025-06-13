# 배열 중 가장 작은 값을 찾아 맨 처음 값이랑 교환
# 요소 개수가 n개이면, 바꾸는 절차를 n-1번 수행

def printStep(A, idx):
    print("   Step %d : " %idx, end="")
    print(A)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if(A[j] < A[least]):
                least = j
        A[i], A[least] = A[least], A[i]
        printStep(A, i + 1)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Before    :", data)

    selectionSort(data)

    print("Selection :", data)
    print()

# 단순함. 효율적 X. 안정성 X
# 시간 복잡도: (n-1) + (n-2) + (n-3) + ... + 1 = n(n-1)/2 = O(n^2)