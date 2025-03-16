class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 1, min(ranks) * cars * cars  # Binary search range

        def canRepairInTime(t):
            total_cars = 0
            for rank in ranks:
                total_cars += isqrt(t // rank)  # Max cars a mechanic can repair in 't' minutes
                if total_cars >= cars:
                    return True
            return False

        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time

        return left
