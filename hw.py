class ParkingGarage:

    tickets = list(range(101))
    parking_spaces = list(range(101))
    current_ticket = {}

    def take_ticket(self, tickets, parking_spaces, current_ticket):
        self.my_ticket = tickets.pop()
        self.my_space = parking_spaces.pop()
        current_ticket = { self : { 'ticket number' : self.my_ticket, 'space number' : self.my_space, 'paid ticket' : False}}
        return current_ticket, self.my_space, self.my_ticket
    
    def pay_for_parking(self, current_ticket):
        payment = input("Please enter payment now. Type [enter] when complete. ").lower()
        if "" not in payment:
            print("The ticket has been paid, you have 15 minutes to leave")
            current_ticket[self]['paid ticket'] = True
        else:
            print("Please try again.")
            self.driver()

    def leave_garage(self, current_ticket, tickets, parking_spaces):
        if current_ticket[self]['paid ticket'] == True:
            print('Thanks You, have a nice day')
            tickets.append(self.my_ticket)
            parking_spaces.append(self.my_space)
        else:
            self.pay_for_parking(current_ticket)

    def driver(self):
        decision = ''
        while 'l' not in decision:
            decision = input('Would you like to, [s]ee how many spots are available, [t]ake a ticket, [c]heck current ticket, [p]ay for a ticket, or [l]eave the garage?: ').lower()
            if 's' in decision:
                print(f'There are {len(self.parking_spaces)} parking spaces.')
            elif 't' in decision:
                self.take_ticket()
            elif 'c' in decision:
               print(f'There are {self.current_ticket[self]}')
            elif 'p' in decision:
                self.pay_for_parking()
            else:
                print('Please choose one of the above options: ')
        self.leave_garage()

user1 = ParkingGarage()

user1.driver()