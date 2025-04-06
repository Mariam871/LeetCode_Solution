from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        value_map = {}

        for id_, val in nums1:
            value_map[id_] = value_map.get(id_, 0) + val

        for id_, val in nums2:
            value_map[id_] = value_map.get(id_, 0) + val

        # Convert the dictionary to a sorted list of [id, value]
        result = [[id_, value_map[id_]] for id_ in sorted(value_map)]
        return result
