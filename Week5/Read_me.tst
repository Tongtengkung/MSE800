Use Case: Make a Table Reservation with Payment

ID:	UC-01
Actor:	Customer
Preconditions:	Customer is logged into the system. Location services are enabled to find nearby restaurants.
Description:	The customer selects a restaurant, date, time, and number of seats. The system displays available slots and total cost. The customer confirms the reservation and proceeds to online payment. Upon successful payment, a reservation confirmation is sent.
Basic Flow:	1. Customer selects "Book a Table."
2. System displays list of restaurants or asks location.
3. Customer picks a restaurant.
4. Customer chooses date and time.
5. System shows available slots and total cost.
6. Customer enters payment details and confirms.
7. System processes payment.
8. Reservation is confirmed, and receipt sent to the customer.
Postconditions:	Reservation is stored in the system with payment confirmation; customer receives notification.
Exceptions:	Payment fails, system prompts to retry. If no slots are available, system suggests alternative times.