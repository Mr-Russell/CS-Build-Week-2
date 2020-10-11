# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# Follow up: The overall run time complexity should be O(log (m+n)).

# Example 1:

  # Input: nums1 = [1,3], nums2 = [2]
  # Output: 2.00000
  # Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

  # Input: nums1 = [1,2], nums2 = [3,4]
  # Output: 2.50000
  # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Example 3:

  # Input: nums1 = [0,0], nums2 = [0,0]
  # Output: 0.00000

# Example 4:

  # Input: nums1 = [], nums2 = [1]
  # Output: 1.00000

# Example 5:

  # Input: nums1 = [2], nums2 = []
  # Output: 2.00000



def findMedianSortedArrays(nums1, nums2):
  list1 = nums1.copy()
  list2 = nums2.copy()
  list1.extend(list2)
  list1.sort()
  
  if len(list1) % 2 == 0:
    median = len(list1) // 2
    return (list1[median-1] + list1[median]) / 2  
      
  else:
    median = (len(list1) // 2)
    return list1[median]  