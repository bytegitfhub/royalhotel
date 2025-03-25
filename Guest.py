class Guest:
    """Represents a guest in the hotel system."""
    
    def __init__(self, name: str, contact: str, loyaltyStatus: str = "Regular"):
        self.__name = name
        self.__contact = contact
        self.__loyaltyStatus = loyaltyStatus

    # Getters
    def getName(self):
        return self.__name

    def getContact(self):
        return self.__contact

    def getLoyaltyStatus(self):
        return self.__loyaltyStatus

    # Setters
    def setContact(self, newContact):
        self.__contact = newContact

    def setLoyaltyStatus(self, newStatus):
        self.__loyaltyStatus = newStatus

    def __str__(self):
        return f"Guest: {self.__name}, Contact: {self.__contact}, Loyalty: {self.__loyaltyStatus}"
