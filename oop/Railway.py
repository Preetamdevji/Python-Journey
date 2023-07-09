# class Train:
#     def __init__(self, train_name, fare, seats):
#         self.train_name = train_name
#         self.fare = fare
#         self.seats = seats
#         self.ticket_list = list(range(1, seats + 1))

#     def get_status(self):
#         print(f"The Name of Train is: {self.train_name}")
#         print(f"The Seats of Train is: {self.seats}")

#     def get_fare(self):
#         print(f"The Fare of Train is Rs: {self.fare}")

#     def booking_ticket(self):
#         if self.seats > 0:
#             ticket_number = self.ticket_list.pop(0)       # remove the first seat
#             self.seats -= 1
#             print(f"Your ticket is booked! Your ticket number is {ticket_number}")
#         else:
#             print("Train is full. Please select another train.")

#     def cancel_ticket(self, ticket_number):
#         if ticket_number in self.ticket_list:
#             self.ticket_list.remove(ticket_number)  # Remove the canceled ticket from the list
#             self.ticket_list.sort()  # Sort the ticket list
#             self.seats += 1  # Increment the number of available seats
#             print(f"Your ticket cancellation number is: {ticket_number}! Your cancellation is successfully done.")
#         else:
#             print("Invalid Number")

#     def ticket_no(self):
#         return len(self.ticket_list)
        
        
# railway = Train("Shalimar Express Of Pakistan", 4520, 10)
# railway.get_status()
# railway.get_fare()
# railway.booking_ticket()
# railway.cancel_ticket(2)
# railway.cancel_ticket(3)
# print(f"Remaining seats: {railway.seats}")
# print(f"Remaining tickets available: {railway.ticket_list}")





class Train:
    def __init__(self,train_name,fare,seats):
        self.train_name = train_name
        self.fare = fare
        self.seats = seats
        self.ticket_list = list(range(1,seats + 1))

    def get_status(self):
        print(f"The Name of Train is:{self.train_name}")
        print(f"The Seats of Train is:{self.seats}")

    def get_fare(self):
        print(f"The Fare of Train is Rs:{self.fare}")

    def booking_ticket(self):
        if (self.seats > 0):
            ticket_number = self.ticket_list.pop(0)       # remove the fist seat
            self.seats = self.seats - 1
            print(f"Your ticket is booked! Your ticket number is {ticket_number}")
        else:
            print("Train is full Please select another train")

    def cancel_ticket(self,ticket_number):
        if ticket_number in self.ticket_list:
            self.ticket_list.append(ticket_number)         #cancelled ticket is addded 
            self.ticket_list.sort()
            self.seats += 1 
            print(f"Your ticket cancellation number is:{ticket_number}!Your cancellation is successfully done:")
        else:
            print("Invalid Number")

    def ticket_no(self):
        return len(self.ticket_list)
        
        
    
railway = Train("Shalimar Express Of Pakistan",4520,10)
railway.get_status()
railway.get_fare()
railway.booking_ticket()
railway.booking_ticket()
railway.booking_ticket()
railway.cancel_ticket(4)
print(f"Remaining seats: {railway.seats}")
print(f"Remainig ticket is avaible: {railway.ticket_list}")
