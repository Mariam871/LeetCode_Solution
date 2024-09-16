# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the Solution class
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify merging
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from either list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the head of the merged list (skip the dummy node)
        return dummy.next

# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))  # 1 -> 2 -> 4
list2 = ListNode(1, ListNode(3, ListNode(5)))  # 1 -> 3 -> 5

# Create a Solution instance and call the method
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)  # 1 -> 1 -> 2 -> 3 -> 4 -> 5
