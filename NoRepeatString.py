#!/usr/bin/python
# -*- coding: utf-8 -*-

# __author__ = 'Administrator'

class NoRepeatString:
    def lengthOfLongestSubString(self,s):

        if not s:
            return 0
        longestLength=1
        substr=""
        for item in s:
            if item not in substr:
                substr+=item
            else:
                if len(substr)>longestLength:
                    longestLength=len(substr)
                #关键点：从重复的下一个字符开始判断(index(item）指的是第一个字符所在位置
                substr+=item
                substr=substr[substr.index(item)+1:]

        if len(substr)>longestLength:
            longestLength=len(substr)

        return longestLength

if __name__== "__main__":
    s='dfafdafdafdaf'
    e=NoRepeatString()
    print(e.lengthOfLongestSubString(s))
