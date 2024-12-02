height = [1,8,6,2,5,4,8,3,7]


#  area = (iright - ileft) * min(height left, height right)
# while l < r
#  if r - l = 2 move the lower height
#  else
#  count area, if l+1 > r-1
#  move left
#  else, move right
#  
def maxArea(height):
    left, right = 0, len(height) - 1
    output = 0

    while left < right:
        print(left, right)
        curArea = (right - left) * min(height[right], height[left])
        output = max(output, curArea)

        if height[left] < height[right]:
            left += 1
        
        else:
            right -= 1

    return output

print(maxArea(height))