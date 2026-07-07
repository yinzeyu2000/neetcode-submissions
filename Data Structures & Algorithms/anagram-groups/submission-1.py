from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res 用来存放分组结果
        # key: 排序后的字符串
        # value: 属于这个 key 的原始字符串列表
        res = defaultdict(list)

        # 遍历每一个字符串
        for s in strs:
            # 把字符串排序，得到统一的 key
            # 例如 eat, tea, ate 排序后都是 aet
            sortedS = ''.join(sorted(s))

            # 把原始字符串加入对应分组
            res[sortedS].append(s)

        # 返回所有分组
        return list(res.values())