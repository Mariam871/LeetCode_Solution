class MyCalendarTwo:

    def __init__(self):
        self.bookings = []   # Store all the bookings
        self.overlaps = []   # Store all the overlaps (i.e., double bookings)

    def book(self, start: int, end: int) -> bool:
        # First check if the new booking overlaps with any of the double bookings (overlaps)
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                # Triple booking found
                return False

        # Now, check for overlaps with existing single bookings
        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:
                # There's an overlap, calculate the new overlap range and add to overlaps
                overlap_start = max(start, booking_start)
                overlap_end = min(end, booking_end)
                self.overlaps.append((overlap_start, overlap_end))

        # If no triple booking was found, add the new booking
        self.bookings.append((start, end))
        return True
