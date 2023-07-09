class Train:
    def __init__(self, full_name, mobile_no, gender, email_address, cnic, payment):
        self.full_name = full_name
        self.mobile_no = mobile_no
        self.gender = gender
        self.email_address = email_address
        self.cnic = cnic
        self.payment = payment

    def show_passenger_info(self):
        print("Full Name:" + " " + self.full_name)
        print("Mobile No:",self.mobile_no)
        print("Gender:",self.gender)
        print("Email Address:", self.email_address)
        print("CNIC:", self.cnic)
        print("Payment:", self.payment)

    def recieve_ticket(self, passenger):
        self.passenger = passenger

    def show_recieve_ticket(self):
        print(self.passenger)

    def your_seat_no(self, seat_no):
        self.seat_no = seat_no

    def show_your_seat_no(self):
        print(self.seat_no)


class Greet(Train):
    def __init__(self, full_name, mobile_no, gender, email_address, cnic, payment,greet):
       super().__init__(full_name, mobile_no, gender, email_address, cnic, payment)
       self.greet = greet
    
    def show_greet(self):
        print(self.greet)

g1 = Greet("Preetam", "1234567890", "Male", "preetam.123e@example.com", "1234567890123", "RS:2500/=", "Thanks for coming to our website")


g1.show_passenger_info()
g1.recieve_ticket("Receive your ticket within two working days")
g1.your_seat_no("Your Seat No is 17 and berth is 4")

g1.show_recieve_ticket()
g1.show_your_seat_no()
g1.show_greet()
