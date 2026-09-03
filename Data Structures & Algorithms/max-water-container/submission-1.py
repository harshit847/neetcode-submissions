class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''max_water = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                width = j - i
                h = min(heights[i],heights[j])
                water = width * h
                max_water = max(water,max_water)
        return max_water'''
        left = 0
        right = len(heights)-1
        maxWater = 0
        while left < right:
            height = min(heights[left],heights[right])
            water = height * (right - left)
            maxWater = max(water,maxWater)
            if heights[left]<heights[right]:
                left += 1
            else:
                right -= 1
        return maxWater

