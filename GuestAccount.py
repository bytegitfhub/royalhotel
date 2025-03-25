class GuestAccount:
    """Handles guest account login and profile updates."""
    
    def __init__(self, email: str, password: str):
        self.__email = email
        self.__password = password
        self.__reservationHistory = []

    # Getters
    def getEmail(self):
        return self.__email

    def getReservationHistory(self):
        return self.__reservationHistory

    # Methods
    def addReservation(self, reservation):
        self.__reservationHistory.append(reservation)

    def __str__(self):
        return f"GuestAccount: {self.__email}, Reservations: {len(self.__reservationHistory)}"
