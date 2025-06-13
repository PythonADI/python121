nums = [11, 23, -9, 4, 45, 231, -90]

print(nums[:2])
print(nums[:5])
print(nums[::2])
print(nums[1::2])
print(nums[::-1])

# nums2 = nums[0:len(nums)]
nums2 = nums[:]

print(f"{nums = }")
print(f"{nums2 = }")
nums2.append(909)
print(f"{nums = }")
print(f"{nums2 = }")

