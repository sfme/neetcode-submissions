
class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack_decrease = []
        res = [0] * len(temperatures)

        for cur_day, temp_val in enumerate(temperatures):

            while stack_decrease and temperatures[stack_decrease[-1]] < temp_val:

                res[stack_decrease[-1]] = cur_day - stack_decrease[-1]

                stack_decrease.pop()

            stack_decrease.append(cur_day)

        return res
            

        

        