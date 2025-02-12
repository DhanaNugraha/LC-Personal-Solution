class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        print(k, nums)
        # make k and nums to be available in other functions in the class by making it self.
        self.k = k
        self.nums = nums
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # append and sort in reverse
        self.nums.append(val)
        self.nums.sort(reverse = True)
        # print(val)
        # print(self.nums)
        
        # return kth largest value
        return self.nums[self.k - 1]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


test = KthLargest(1,2).add(3)
print(test)

