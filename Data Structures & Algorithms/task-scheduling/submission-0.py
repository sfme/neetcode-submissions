import heapq

from collections import Counter, deque

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_counts_map = Counter(tasks)

        max_heap = [-count for count in  task_counts_map.values()]
        heapq.heapify(max_heap)

        cool_off_queue = deque()

        time = 0

        while cool_off_queue or max_heap:
            time += 1

            if max_heap:
                current_count = heapq.heappop(max_heap) + 1

                if current_count != 0:
                    cool_off_queue.appendleft((time + n, current_count))

            if cool_off_queue and cool_off_queue[-1][0] == time:

                heapq.heappush(max_heap, cool_off_queue.pop()[1])

        return time



            



