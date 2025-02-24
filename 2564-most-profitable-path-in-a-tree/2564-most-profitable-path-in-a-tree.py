from typing import List
from collections import defaultdict

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Step 1: Build the tree as an adjacency list
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        # Step 2: Find Bob's path to node 0 and track time taken to reach each node
        step_bob = {}  # Stores the time Bob reaches each node

        def dfs_bob(node, parent, time):
            """DFS to determine when Bob reaches each node on the path to 0"""
            step_bob[node] = time  # Record Bob's arrival time at node
            if node == 0:  # Reached the root
                return True
            for neighbor in tree[node]:
                if neighbor != parent and dfs_bob(neighbor, node, time + 1):
                    return True
            del step_bob[node]  # Remove if not on the path to 0
            return False

        dfs_bob(bob, -1, 0)  # Start DFS from Bob’s node

        # Step 3: DFS for Alice’s optimal path
        def dfs_alice(node, parent, time, income):
            """
            DFS to find the maximum net income Alice can achieve.
            """
            # Compute Alice's profit at this node
            if node in step_bob:
                bob_time = step_bob[node]
                if bob_time == time:
                    income += amount[node] // 2  # Alice & Bob share
                elif bob_time > time:
                    income += amount[node]  # Alice arrives first, takes full amount
            else:
                income += amount[node]  # Bob never visits, Alice gets full amount
            
            # Leaf node check: If no other unvisited child, return income
            is_leaf = True
            max_income = float('-inf')
            for neighbor in tree[node]:
                if neighbor != parent:
                    is_leaf = False
                    max_income = max(max_income, dfs_alice(neighbor, node, time + 1, income))
            
            return max_income if not is_leaf else income  # If leaf, return final income
        
        return dfs_alice(0, -1, 0, 0)  # Start DFS from root
