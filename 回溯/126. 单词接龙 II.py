#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/7 10:54 下午
 @Author   :pulinghao@baidu.com
 @File     :126. 单词接龙 II.py 
 @Description :
"""
import string
from collections import defaultdict
from collections import deque


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_set = set(wordList)
        res = []
        if len(wordList) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        found = self.bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res

        path = [beginWord]
        self.dfs(beginWord, endWord, successors, path, res)
        return res

    def bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                next_level_visited.add(next_word)
                                queue.append(next_word)
                                successors[current_word].add(next_word)

                    word_list[j] = origin_char
            if found:
                break
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_word = successors[beginWord]
        for next_word in successor_word:
            path.append(next_word)
            self.dfs(next_word, endWord, successors, path, res)
            path.pop(-1)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    solution = Solution()
    res = solution.findLadders(beginWord, endWord, wordList)
    print(res)
