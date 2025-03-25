class Payment:
    """Handles payment transactions."""
    
    def __init__(self, method: str, amount: float, transactionId: str):
        self.__method = method
        self.__amount = amount
        self.__transactionId = transactionId

    def __str__(self):
        return f"Payment: {self.__method} | Amount: ${self.__amount} | Transaction ID: {self.__transactionId}"
