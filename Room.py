class Room:
    """Represents a hotel room."""
    
    def __init__(self, roomNumber: int, roomType: str, amenities: list, price: float):
        self.__roomNumber = roomNumber
        self.__roomType = roomType
        self.__amenities = amenities
        self.__price = price
        self.__available = True  # Initially available

    # Getters
    def getRoomNumber(self):
        return self.__roomNumber

    def getRoomType(self):
        return self.__roomType

    def isAvailable(self):
        return self.__available

    # Methods
    def bookRoom(self):
        """Marks the room as unavailable."""
        self.__available = False

    def releaseRoom(self):
        """Marks the room as available again."""
        self.__available = True

    def __str__(self):
        status = "Available" if self.__available else "Booked"
        return f"Room {self.__roomNumber}: {self.__roomType} - {status}"
