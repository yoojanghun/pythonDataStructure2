# 버블 정렬
# 인접한 2개의 레코드를 비교하여 크기가 순서대로가 아니면 서로 교환
# 비교-교환 과정을 리스트의 전체에 수행. 한번의 스캔이 완료되면 리스트의 오른쪽 끝에 가장 큰 레코드
# 끝으로 이동한 레코드를 제외하고 다시 스캔 반복

def printStep(A, idx):
    print("   Step %d : " %idx, end="")
    print(A)

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        flag = False
        for j in range(1, n-i):
            if (A[j-1] > A[j]):
                A[j-1], A[j] = A[j], A[j-1]
                flag = True

        if not flag:
            break

        printStep(A, i+1)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
    print("Before    :", data)

    bubbleSort(data)

    print("Selection :", data)
    print()

# 시간 복잡도: O(n^2)
# 최상, 평균, 최악의 경우 모두 일정