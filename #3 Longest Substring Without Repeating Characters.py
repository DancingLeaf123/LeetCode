
        max_str = ""
        match_str = ""
        result = 0
        bf_index = 0
        match_bf_index = 0
        # s = "dd 2"
        if s == "":
            result = 0

        if s != "":
            for count, item in enumerate(s):
                # print("count","item", count, item)
                if item not in max_str and (count - bf_index) <= 1 :
                    max_str += item
                    bf_index = count
                    match_str = max_str[1:] 
                    # match_str = (max_str[1:] if (match_str == "") else match_str)
                    match_bf_index = count
                elif item not in match_str and (count - (match_bf_index if match_bf_index != 0 else bf_index)) <= 1:
                    match_str += item
                    match_bf_index = count
                    if len(match_str) > len(max_str):
                        max_str = match_str
                        bf_index = count
                        match_bf_index = count
                        match_str = ""
                elif item in match_str and len(match_str) == 1:
                    match_str = item
                    match_bf_index = count
                                       
                print("max_str",max_str)
                print("match_str",match_str)
                print("match_bf_index",match_bf_index)
                print("count",count)
            result = len(max_str)
        # print (max_str,result)
        return result 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        
        mylist = s
        uni_mylist = list(dict.fromkeys(mylist))
        if len(uni_mylist) == 1:
            return 1
        print ("uni_mylist",uni_mylist)
        longest_str = ""
        longest = 0
        for i, x  in enumerate(uni_mylist):
            split_list = mylist.split(x)
            print ("split_list",split_list)
            for i in split_list:
                if len(i) == len(list(dict.fromkeys(i))):
                    sm_lf = mylist[mylist.index(i) - 1]
                    sm_rt = mylist[mylist.index(i) + len(i)]
                    if len(i) > longest or (len(i) == longest and (sm_lf != sm_rt) and sm_lf in range(0,len(mylist))  and sm_rt in range(0,len(mylist))):
                        print ("len(i)",len(i))
                        print ("longest",longest)
                        print ("sm_lf",sm_lf)
                        print ("sm_rt",sm_rt)
                        longest_str = i
                        longest = len(i)
                        
        if mylist.count(longest_str) > 1:
            useindex = mylist.index(longest_str,1)
        else:
            useindex = mylist.index(longest_str)
        lf = None
        rt = None
        if 0 <= useindex - 1 < len(mylist):
            lf = (mylist[useindex - 1] if mylist[useindex - 1] else None)
            
        if 0 <= useindex + len(longest_str) < len(mylist):
            rt = (mylist[useindex + len(longest_str)] if mylist[useindex +  + len(longest_str)] else None)       
        print ("badd",longest_str, longest)          

        if lf and lf not in longest_str:
            longest_str = lf + longest_str
            longest  += 1
        if rt and rt and rt not in longest_str:
            longest_str = longest_str + rt
            longest  += 1
        print (longest_str, longest)
        return longest




