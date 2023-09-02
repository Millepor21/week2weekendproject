class ParkingGarage:

    tickets = list(range(2))
    parking_spaces = list(range(2))
    current_ticket = {}

    def take_ticket(self, tickets, parking_spaces):
        self.my_ticket = tickets.pop()
        self.my_space = parking_spaces.pop()
        self.current_ticket = {'ticket number' : self.my_ticket, 'space number' : self.my_space, 'paid ticket' : False}
        return self.current_ticket, self.my_space, self.my_ticket
    
    def pay_for_parking(self):
        self.payment = input("Please enter payment now. Type [enter] when complete. ").lower()
        if self.payment == 'enter':
            print("The ticket has been paid, you have 15 minutes to leave")
            self.current_ticket['paid ticket'] = True
        else:
            print("Please try again.")
            self.driver()

    def leave_garage(self):
        if 'paid ticket' in self.current_ticket and self.current_ticket['paid ticket'] == True:
            print('Thanks You, have a nice day')
            self.tickets.append(self.my_ticket)
            self.parking_spaces.append(self.my_space)
        else:
            self.pay_for_parking()

    def driver(self):
        decision = ''
        while 'l' not in decision:
            decision = input('Would you like to, [s]ee how many spots are available, [t]ake a ticket, [c]heck current ticket, [p]ay for a ticket, or [l]eave the garage?: ').lower()
            if 's' in decision:
                print(f'There are {len(self.parking_spaces) - 1} parking spaces.')
            elif 't' in decision:
                self.take_ticket(self.tickets, self.parking_spaces)
            elif 'c' in decision:
               print(f'Your ticket number is {self.current_ticket["ticket number"]} and your parking space is {self.current_ticket["space number"]}')
            elif 'p' in decision:
                self.pay_for_parking()
            else:
                print('Please choose one of the above options: ')
        self.leave_garage()

user1 = ParkingGarage()

user1.driver()