s = "gppsludzdtmccibi"
temp_lstr = ""
temp_long = 0
match_lstr = ""
match_long = 0
m_s_i = 0
longest_start_index = 0
last_point = 0
for i, x in enumerate(s):
    if x not in temp_lstr and i - last_point <= 1:
        temp_lstr += x
        temp_long = len(temp_lstr)
        last_point = i
    else:
        # print("0m_s_i", m_s_i)
        # m_s_i = (s.index(x, m_s_i) + 1 if m_s_i == 0 else m_s_i)     
        if x in temp_lstr or x in match_lstr:
            print ("in m_s_i", m_s_i)
            j_s = s.index(x, m_s_i) + 1
            j_e = i + 1
            print ("j_s", j_s)
            print ("j_e", j_e)
            for j in range(j_s, j_e):
                if s[j] == x and m_s_i < j:
                    m_s_i = j
                    break
                if s[j] != x:
                    m_s_i = j
                    print("m_s_i", m_s_i)
                    break
        else:
            m_s_i = m_s_i
        # m_s_i = (s.index(x, m_s_i) + 1 if x in temp_lstr else m_s_i)
        print("1m_s_i", m_s_i)
        print("i", i)
        # m_s_i = (m_s_i if m_s_i >= longest_start_index else longest_start_index)
        # print("2m_s_i", m_s_i)
        match_lstr = (s[m_s_i: i+1])
        match_long = len(match_lstr)
        if len(match_lstr) >= temp_long:
            temp_lstr = match_lstr
            temp_long = len(match_lstr)
        # else:
        #     longest_start_index = s.index(x, m_s_i) + 1
        #     print("longest_start_index", longest_start_index)
    print("temp_lstr", temp_lstr)
    print("match_lstr", match_lstr)
    print("-------------")

print("temp_lstr", temp_lstr)
print("temp_long", temp_long)
    


