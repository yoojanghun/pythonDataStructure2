# 선형 조사법
# 충돌이 일어나면 해시 테이블의 다음 위치에 저장

# 빈 버킷을 두 가지로 분류
# 한번도 사용하지 않은 것 => 0
# 사용 되었다가 삭제되어 현재 비어있는 것 => -1

# 버킷의 숫자는 소수
# 선형 조사법, 이차 조사법, 이중 해싱법
# 이중 해싱법: 충돌 발생시, 다른 해시 함수를 이용해 다음 위치 계산
M = 13

class HashTable:
    def __init__(self):
        self.table = [0] * M

    def hashFn(self, key):
        return key % M

    def hashFn2(self, key):
        return 11 - (key % 11)

    def insert(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M
            # bucket = (hashVal + i**2) % M       # 2차 조사법 (Quadratic proving)
            bucket = (hashVal + i * self.hashFn2(key)) % M      # 이중 해싱법

            if self.table[bucket] == 0:
                self.table[bucket] = key
                break

    def search(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M
            # bucket = (hashVal + i**2) % M       # 2차 조사법 (Quadratic proving)
            bucket = (hashVal + i * self.hashFn2(key)) % M  # 이중 해싱법

            if self.table[bucket] == 0:
                return -1
            elif self.table[bucket] == key:
                return bucket

    def delete(self, key):
        hashVal = self.hashFn(key)

        for i in range(M):
            # bucket = (hashVal + i) % M
            # bucket = (hashVal + i**2) % M       # 2차 조사법 (Quadratic proving)
            bucket = (hashVal + i * self.hashFn2(key)) % M  # 이중 해싱법

            if self.table[bucket] == 0:
                print("No key to delete")
                return
            elif self.table[bucket] == key:
                print("Delete Key(%d) at bucket(%d). " % (key, bucket))
                self.table[bucket] = -1
                return


if __name__ == "__main__":

    HT = HashTable()
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]

    for d in data:
        print("h(%d) = %2d " % (d, HT.hashFn(d)))
        HT.insert(d)
        print(HT.table)

    print()
    print("Search(60) ---> ", HT.search(60))

    HT.delete(9)
    print(HT.table)

    print("Search(46) --> ", HT.search(46))