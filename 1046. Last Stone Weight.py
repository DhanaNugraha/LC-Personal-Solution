# heap sort
import heapq

stones = [2,7,4,1,8,1]

def lastStoneWeight(stones):
    new_stones = []
    for stone in stones:
        heapq.heappush(new_stones, -1 * stone)

    while len(new_stones) > 1:
        y = heapq.heappop(new_stones)
        x = heapq.heappop(new_stones)
        if x != y:
            heapq.heappush(new_stones, (y - x))
            print(new_stones)
        else:
            continue

    if len(new_stones) == 0:
        return 0
    else: 
        return new_stones[0] * -1


print(lastStoneWeight(stones))




# works but leetcode dont have this
# def lastStoneWeight(stones):
#     heapq._heapify_max(stones)
#     while len(stones) > 1:
#         y = heapq._heappop_max(stones)
#         x = heapq._heappop_max(stones)
#         if x != y:
#             stones.append(y - x)
#             heapq._siftdown_max(stones, 0, len(stones) - 1)
#         else:
#             continue
#     return stones[0]

# print(lastStoneWeight(stones))
