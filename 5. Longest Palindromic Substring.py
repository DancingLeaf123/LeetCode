def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    temp_l = s

    # lf_index = (lf_index + 1 if lf_index + 1 <= len(tl_pldrm) - 1 else lf_index)
    # rt_index = len(tl_pldrm) -1 - lf_index
    flag = 0
    for i in range(0, len(s)//2 + 1):
        lf = i
        rt = len(s)-1
        if temp_l[lf] != temp_l[rt]:
            rt = (rt -1 if rt > lf else rt)
            continue
        else:
            temp_l

            
            

    print ("tl_pldrm", tl_pldrm)
    return tl_pldrm

s = "ssdad"
longestPalindrome(s)    