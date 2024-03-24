""" 
    sol2

    [0,1,0,2,1,0,1,3,2,1,2,1]

    가장 높은 수를 찾음 그것이 두개 이상이 아니라면 -1

    [0,1,0,2,1,0,1,2,2,1,2,1]

    가장 높은 수가 여러개일 경우 해당 숫자 사이의 작은값들의 수를 계산

    [0,1,0,2,1,0,1,2,2,1,2,1]
    3개, 1개
    
    그 이후 가장 높은수들을 전부 -1

    [0,1,0,1,1,0,1,1,1,1,1,1]

    2개

    3+1+2=6
"""

# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         water = 0  # 빗물 양
#         temp_max = max(height)  # 현최고 높이

#         # 맨위부터 하나씩
#         for m in reversed(range(1, temp_max + 1)):
#             # 최대 높이가 하나일 경우
#             if height.count(m) == 1:
#                 # 최대숫자 -1하기
#                 height[height.index(m)] -= 1

#             # 최대 높이가 둘 이상인 경우
#             else:
#                 # 맨앞 큰수 찾기
#                 front = height.index(m)
#                 # 맨뒤 큰수 찾기
#                 for i in reversed(range(len(height))):
#                     if height[i] == m:
#                         back = i
#                         break

#                 # 중간 물 찾기 & 한층 아래로
#                 for i in range(front, back + 1):
#                     if m > height[i]:
#                         water += 1
#                     elif m == height[i]:
#                         height[i] -= 1

#         return water


class Solution(object):
    def trap(self, height):
        n = len(height)
        left, right, max_val, water = 0, n - 1, 0, 0

        while left < right:
            if height[left] <= height[right]:
                max_val = max(max_val, height[left])
                if height[left] >= max_val:
                    water += max_val - height[left]
                    height[left] = max_val - 1
                left += 1
            else:
                max_val = max(max_val, height[right])
                if height[right] >= max_val:
                    water += max_val - height[right]
                    height[right] = max_val - 1
                right -= 1

        return water


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
