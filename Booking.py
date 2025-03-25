from datetime import datetime

class Booking:
    """Handles guest room reservations."""
    
    def __init__(self, guest, room, checkIn: str, checkOut: str):
        self.__guest = guest
        self.__room = room
        self.__checkIn = datetime.strptime(checkIn, "%Y-%m-%d")
        self.__checkOut = datetime.strptime(checkOut, "%Y-%m-%d")
        self.__status = "Confirmed"

    # Methods
    def cancelBooking(self):
        """Cancels the booking and releases the room."""
        self.__status = "Cancelled"
        self.__room.releaseRoom()

    def __str__(self):
        return f"Booking for {self.__guest.getName()} in Room {self.__room.getRoomNumber()} ({self.__status})"
