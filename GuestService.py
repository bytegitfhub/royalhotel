class GuestService:
    """Handles guest service requests."""
    
    def __init__(self, requestType: str):
        self.__requestType = requestType
        self.__status = "Pending"

    def completeRequest(self):
        self.__status = "Completed"

    def __str__(self):
        return f"Service Request: {self.__requestType} - {self.__status}"
