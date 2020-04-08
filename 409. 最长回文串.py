#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/3/31 10:12 下午
 @Author   :pulinghao@baidu.com
 @File     :最长回文串.py 
 @Description :
 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 1:
            return 1
        array = []
        for i in range(52):
            array.append(0)

        for char in s:
            if ord(char) > ord('Z'):
                index = ord(char) - ord('a') + 26
            else:
                index = ord(char) - ord('A')
            array[index] += 1

        # 遍历数组
        length = 0
        for count in array:
            if count % 2 == 0:
                length = count + length
            else:
                length = length + count - 1

        if length < len(s):
            return length + 1
        else:
            return length


if __name__ == '__main__':
    s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
    ret = Solution().longestPalindrome(s)
    print ret
