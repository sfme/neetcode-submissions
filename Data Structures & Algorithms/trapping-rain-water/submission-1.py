
class Solution:

    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        left_max_list = [height[0]] * len(height)
        for jj in range(1, len(height)):
            left_max_list[jj] = max(left_max_list[jj-1], height[jj])

        right_max_list = [height[-1]] * len(height)
        for jj in range(len(height)-2, -1 , -1):
            right_max_list[jj] = max(right_max_list[jj+1], height[jj])

        area_water = 0
        for ii in range(1, len(height)-1):
            area_water += min(left_max_list[ii], right_max_list[ii]) - height[ii]

        return area_water


              

            





        