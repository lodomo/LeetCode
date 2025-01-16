class List(list):
    pass

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        numset = set()
        n = len(A)
        result = [0]
        print(numset)

        for i in range(n):
            result.append(result[-1])
            if A[i] == B[i]:
                result[-1] += 1
                continue

            print(numset)
            if A[i] in numset:
                result[-1] += 1
            else:
                numset.add(A[i])

            print(numset)
            if B[i] in numset:
                result[-1] += 1
            else:
                numset.add(B[i])

        return result[1:]

A = [1,3,2,4]
B = [3,1,2,4]

Solution().findThePrefixCommonArray(A, B)
