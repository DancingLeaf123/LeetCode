

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    result = float(0)
    two_arr = nums1 + nums2
    two_arr.sort()
    # print("two_arr", two_arr)
    # print("len(two_arr)//2", len(two_arr)//2)
    # ifOdd = (len(two_arr)/2 if len(two_arr)/2 else None)
    if len(two_arr) % 2 == 0:
        result = two_arr[len(two_arr)//2 - 1] + two_arr[len(two_arr)//2]
        print("b", result)
        result = result / 2
    else:
        result = two_arr[len(two_arr)//2]
    
    result = float(result)
    print("result", result)
    return result


nums1 = [1,2]
nums2 = [3,4]
findMedianSortedArrays(nums1, nums2)

