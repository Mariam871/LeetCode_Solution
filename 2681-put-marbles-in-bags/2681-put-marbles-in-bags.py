class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0 #No partitions, so min and max scores are the same.
        pair_sums = [weights[i] + weights[i+1] for i in range(len(weights)- 1)]
        return sum(nlargest(k-1, pair_sums)) - sum(nsmallest(k-1, pair_sums))
        