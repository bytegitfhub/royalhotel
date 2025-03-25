class Feedback:
    """Stores guest feedback and ratings."""
    
    def __init__(self, guest, rating: int, comments: str):
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments

    def __str__(self):
        return f"Feedback from {self.__guest.getName()}: {self.__rating}/5 - {self.__comments}"
