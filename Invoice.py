class Invoice:
    """Represents an invoice for a booking."""
    
    def __init__(self, booking, additionalCharges=0, discount=0):
        self.__booking = booking
        self.__totalAmount = booking._Booking__room.getPrice() + additionalCharges - discount

    def __str__(self):
        return f"Invoice: {self.__totalAmount} (Booking: {self.__booking})"
