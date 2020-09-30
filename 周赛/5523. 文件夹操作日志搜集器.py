    #!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/27 10:36 上午
@Author:  pulinghao
@File: 5523. 文件夹操作日志搜集器.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for log in logs:
            if log == '../':
                if len(stack) > 0:
                    stack.pop(-1)

            elif log == './':
                continue
            else:
                stack.append(log)

        return len(stack)

if __name__ == '__main__':
    logs = []

    out = Solution().minOperations(logs)

    print out
