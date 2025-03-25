class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Step 1: Sort the meetings by the start day
        meetings.sort()

        # Step 2: Merge overlapping meetings
        merged_meetings = []
        
        for meeting in meetings:
            if not merged_meetings or merged_meetings[-1][1] < meeting[0]:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])

        # Step 3: Calculate total days occupied by meetings
        meeting_days = 0
        for start, end in merged_meetings:
            meeting_days += (end - start + 1)

        # Step 4: Calculate free days by subtracting meeting days from total available days
        free_days = days - meeting_days
        return free_days
