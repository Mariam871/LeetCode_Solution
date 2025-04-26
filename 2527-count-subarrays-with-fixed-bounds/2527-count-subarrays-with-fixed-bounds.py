class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        lastMin = lastMax = badIdx = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                badIdx = i
            if num == minK:
                lastMin = i
            if num == maxK:
                lastMax = i

            answer += max(0, min(lastMin, lastMax) - badIdx)

        return answer
