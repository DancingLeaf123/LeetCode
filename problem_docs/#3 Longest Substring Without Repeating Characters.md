3. Longest Substring Without Repeating Character

`s` consists of English letters, digits, symbols and spaces.

return type is  integer a number 0~max

if only " "   return 0

if  in other situation,  return longest length of string.

for this situation  "pwwkew" pwke is worng.  

```md
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

for a  s like this  "pwwkew"

emmmmmmmmm  我觉得之前的思路都不对, 

我再来想想吧.

"abcabcbb"
"bbbbb"
"bbcbb"
"pwwkew"
"bbtablud"
""
"ohvhjdml"
我们的已知信息有哪些?

len (s)
1
2
3
3
4

[0:count]
[count+1, s.index(count +1,len(s))]

len = 8




