nums = [1, 2, 3]
nums.append(4)
nums.insert(0, 0)
nums[2] = 10
removed = nums.pop()        # removes last
is_three = 3 in nums
print("nums:", nums)
print("removed:", removed, "contains 3:", is_three)

from Signature_folder.Signature import sign
sign()