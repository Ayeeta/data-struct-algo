def median(num1, num2):
    merged_list = num1 + num2
    merged_list.sort()
    if len(merged_list)/2 != 0:
        return sum(merged_list)/len(merged_list)
        
    else:
        mid_point = len(merged_list)//2
        return  sum(merged_list[mid_point-1] + merged_list[mid_point])/2
         
nums1 = [1, 2]
nums2 = [3, 4]

print(median(nums1, nums2))