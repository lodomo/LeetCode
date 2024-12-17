import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        map = {}
        heap = []
        for c in s:
            if c not in map:
                map[c] = 0
            map[c] += 1
        for key in map:
            heapq.heappush(heap, (-ord(key), map[key]))

        new_string = []
        at_limit = False
        while heap:
            if at_limit:
                hold = heapq.heappop(heap)
                if not heap:
                    continue
                char, count = heapq.heappop(heap)
                new_string.append(chr(-char))
                count -= 1
                if count:
                    heapq.heappush(heap, (char, count))
                heapq.heappush(heap, hold)
                at_limit = False
                continue

            char, count = heapq.heappop(heap)
            if count > repeatLimit:
                new_string.append(chr(-char) * repeatLimit)
                count -= repeatLimit
                heapq.heappush(heap, (char, count))
                at_limit = True
            else:
                new_string.append(chr(-char) * count)

        return "".join(new_string)

s = "cczazcc"
target = 3

sol = Solution()
print(sol.repeatLimitedString(s, target))

