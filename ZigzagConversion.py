#!/usr/bin/python
# -*- coding: utf-8 -*-

# __author__ = 'Administrator'
#判断是否回文数
class ZigzagConversion:
    def convert(self,s,numRows):
        if numRows<=1:
            return s
        res = ""
        size = 2 * numRows - 2
        for i in range(numRows):
            R=list(range(len(s)))
            for j in R[i:len(s):size]:
                res += s[j]
                tmp = j + size - 2 * i
                if i!=0 and i!=numRows-1 and tmp<len(s):
                    res+=s[tmp]
        return res
if __name__=="__main__":
    zigzag=ZigzagConversion()
    print(zigzag.convert('PAYPALISHIRING',3))



