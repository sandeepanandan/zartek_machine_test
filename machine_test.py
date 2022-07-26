class Solution(object):
   def answer(self, nums, target):
      check = {}
      for i in range(len(nums)):
         if target - nums[i] in check:
            return [check[target - nums[i]],i]
         else:
            check[nums[i]]=i
    

input_list = [4,8,14,3]
ob1 = Solution()
print(ob1.answer(input_list, 17))