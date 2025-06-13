class SortedArraySet:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True

        return False

    def insert(self, e):
        if self.contains(e) or self.isFull():
            return

        self.array[self.size] = e
        self.size += 1

        for i in range(self.size-1, 0, -1):
            if self.array[i-1] < self.array[i]:
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    def delete(self, e):
        if not self.contains(e):
            return

        i = 0
        while self.array[i] < e:
            i += 1

        self.size -= 1

        while i < self.size:
            self.array[i] = self.array[i+1]
            i += 1

    def union(self, setB):
        setC = SortedArraySet()
        i = 0       # 집합A 순회
        j = 0       # 집합B 순회

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]

            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1

        while j < setB.size:
            setC.append(setB.array[j])
            j += 1

        return setC

if __name__ == '__main__':
    import random
    setA = SortedArraySet()
    for i in range(5):
        setA.insert(random.randint(1, 9))

    print('Set A : ', setA)

# 집합의 원소들을 배열에 정렬하여 관리함
# 연산들의 성능에 차이가 발생
# 삽입 연산은 더 복잡해 짐
# 원소가 집합에 포함되어 있는지 검사 => 효율적 구현 가능
# 집합의 비교나 합집합, 차집합, 교집합 => 효율적 구현 가능

# 삽입 과정
# 중복 검사: O(n)
# 삽입할 위치 찾기: O(n)
# 해당 위치에 삽입: O(n)