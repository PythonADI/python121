"""

list = [
    element to save in list
    from where to take that element
    conditionalv (can be ommited)
]
"""
nums = [1, 7, -5, 12, 13, 8]

# nums2 = []

# for num in nums:
#     nums2.append(num ** 2)

nums2 = [
    num ** 2
    for num in nums
]

print(nums2)
