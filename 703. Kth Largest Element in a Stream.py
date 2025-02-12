import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        # make k and nums to be available in other functions in the class by making it self.
        self.k = k
        self.nums = nums
        # https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
        heapq.heapify(self.nums)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        

    def add(self, val):
        heapq.heappush(self.nums, val)
        # edge case just in case the length of nums is greater than k
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


test = KthLargest(1,2).add(3)
print(test)

