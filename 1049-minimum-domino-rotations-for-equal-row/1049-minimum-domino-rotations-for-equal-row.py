from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        res = check(tops[0])
        if res != -1 or tops[0] == bottoms[0]:
            return res
        return check(bottoms[0])
