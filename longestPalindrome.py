#!/user/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def longestParindrome(self,s):
        if not s:
            return ''
        if len(s)==1:
            return s
        subString=''
        length=2
        list=[]
        while(length<=len(s)):
            for i in range(len(s)-length+1):
                subString=s[i:i+length]
                if subString==subString[::-1]:
                    list.append(subString)
                    break
            length+=1
        if list:
            return list[-1]
        else:
            return s[0]


if __name__=="__main__":
    s='abcda'
    solution=Solution()
    print(solution.longestParindrome(s))

