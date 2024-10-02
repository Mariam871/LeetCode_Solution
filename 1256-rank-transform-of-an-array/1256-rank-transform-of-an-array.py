class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    # Step 1: Sort the unique elements of the array
        sorted_unique = sorted(set(arr))

    # Step 2: Create a mapping from element to rank
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}

    # Step 3: Replace each element in the array with its rank
        return [rank_map[num] for num in arr]   
        