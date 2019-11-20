def merge_arr(nums1, m,  nums2, n):
    nums1[m:] = nums2
    nums1.sort()