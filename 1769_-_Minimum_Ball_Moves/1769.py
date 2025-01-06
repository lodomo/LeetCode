class List(list):
    pass

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = list(map(int, boxes))
        move_right = [0] * n
        move_left = [0] * n
        results = [0] * n

        cur_balls = 0
        for i in range(1, n):
            move_right[i] = (cur_balls + move_right[i-1])
            cur_balls += boxes[i]

        cur_balls = 0
        for i in range(n-1, -1, -1):
            move_left[i] = (cur_balls + move_left[i+1]) if i < n-1 else 0
            cur_balls += boxes[i]

        for i in range(n):
            results[i] = move_right[i] + move_left[i]

        return results

boxes = "001011"
print(Solution().minOperations(boxes))
