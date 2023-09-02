class ParkingGarage:

    tickets = list(range(101))
    parking_spaces = list(range(101))
    current_ticket = {}

    def take_ticket(self, tickets, parking_spaces, current_ticket):
        self.my_ticket = tickets.pop()
        self.my_space = parking_spaces.pop()
        current_ticket = { self : { 'ticket number' : self.my_ticket, 'space number' : self.my_space, 'paid ticket' : False}}
        current_ticket = { self : { 'ticket number' : self.my_ticket, 'space number' : self.my_space, 'paid' : False}}
        return current_ticket
    
    def pay_for_parking(self, current_ticket):
        payment = input("Please enter payment now. Type [enter] when complete. ").lower()
        if "" not in payment:
            print("The ticket has been paid, you have 15 minutes to leave")
            current_ticket[self]['paid ticket'] = True
        else:
            print("Please try again.")
            self.driver()

    def leave_garage(self):
        pass

    def driver(self):
        decision = ''
        while 'l' not in decision:
            decision = input('Would you like to, [s]ee how many spots are available, [t]ake a ticket, [c]heck current ticket, [p]ay for a ticket, or [l]eave the garage?: ').lower()
            if 's' in decision:
                pass
            elif 't' in decision:
                pass
            elif 'c' in decision:
                pass
            elif 'p' in decision:
                pass
            elif 'l' in decision:
                pass
            else:
                print('Please choose one of the above options: ')

user1 = ParkingGarage()

print(user1.take_ticket([1,2,3], [1,2,3],{}))