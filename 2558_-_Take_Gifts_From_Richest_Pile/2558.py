import heapq
from math import sqrt


class List(list):
    pass


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i, gift in enumerate(gifts):
            gifts[i] = -gift

        heapq.heapify(gifts)

        for _ in range(k):
            gift = heapq.heappop(gifts)
            gift = int(sqrt(-gift))
            heapq.heappush(gifts, -gift)

        return -sum(gifts)



gifts = [25, 64, 9, 4, 100]
k = 4

print(Solution().pickGifts(gifts, k))
