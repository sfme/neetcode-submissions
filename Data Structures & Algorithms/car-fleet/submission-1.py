
class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # sorted by dist; increasing elems = (dist, time)
        cars_stack = sorted([(a, (target - a) / b) for a, b in zip(position, speed)], key=lambda x: x[0])

        num_fleet = 0

        while cars_stack:
            car_lead_time = cars_stack.pop()[1]
            num_fleet += 1

            while cars_stack and cars_stack[-1][1] <= car_lead_time:
                cars_stack.pop()
        
        return num_fleet



        