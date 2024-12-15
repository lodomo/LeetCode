import heapq

class List(list):
    pass

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []
        heapq.heapify(heap)

        for class_room in classes:
            new_room = self.create_room(class_room)
            print(new_room)
            heapq.heappush(heap, new_room)
        
        for _ in range(extraStudents):
            room = heapq.heappop(heap)
            room[1] += 1
            room[2] += 1
            room[0] = self.calculate_benefit([room[1], room[2]])
            heapq.heappush(heap, room)

        return sum([room[1] / room[2] for room in heap]) / len(heap)

    def create_room(self, data):
        benefit = self.calculate_benefit(data)
        return [benefit, data[0], data[1]]

    def calculate_benefit(self, data):
        if data[0] == data[1]:
            return 0
        this_room = data[0] / data[1]
        next_room = (data[0] + 1) / (data[1] + 1)
        return this_room - next_room

classes = [[1,2],[3,5],[2,2]]
extra_students = 2

print(Solution().maxAverageRatio(classes, extra_students))
