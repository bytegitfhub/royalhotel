from Guest import Guest
from Room import Room
from Booking import Booking
from Payment import Payment
from GuestService import GuestService
from Feedback import Feedback

# Creating a guest
guest1 = Guest("James Alaine", "+1 787-456-823")

# Creating a room
room1 = Room(101, "Deluxe", ["WiFi", "TV", "Mini-Bar"], 150)

# Making a booking
booking1 = Booking(guest1, room1, "2025-03-10", "2025-03-15")
print(booking1)

# Processing payment
payment1 = Payment("Credit Card", 750, "TXN12345")
print(payment1)

# Guest leaves feedback
feedback1 = Feedback(guest1, 5, "Excellent service!")
print(feedback1)
