class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0

        for x, freq in count.items():
            group_size = x + 1
            # Number of full groups needed for freq rabbits each saying x
            num_groups = (freq + x) // group_size
            total += num_groups * group_size

        return total
