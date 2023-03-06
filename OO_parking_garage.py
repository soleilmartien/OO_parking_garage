class Garage():
    def __init__(self,tickets, parkingSpaces, currentTicket, ticketPrice):
        self.tickets = tickets
        self.ticketPrice = ticketPrice
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
        self.currentTicket['amountdue'] = ticketPrice
    def takeTicket(self):
        self.tickets.remove(self.currentTicket['parkingPlaceNumber'])
        self.parkingSpaces.remove(self.currentTicket['parkingPlaceNumber'])
    def payForParking(self):
        payamount = -self.currentTicket['amountdue']
        payamount += int(input('You have '+str(self.currentTicket['amountdue'])+'$ to pay. Enter the amount you want to pay.'))
        if payamount >= 0:
            print('You ticket: '+self.currentTicket['parkingPlaceNumber']+ ' has been paid, you have 15 minutes to leave.')
            self.currentTicket['paid'] = True
            self.currentTicket['amountdue'] = 0
    def leaveGarage(self):
        if self.currentTicket['paid'] == True:
            print('Thank you, have a nice day!')
            self.tickets.append(self.currentTicket['parkingPlaceNumber'])
            self.parkingSpaces.append(self.currentTicket['parkingPlaceNumber'])
        else:
            Garage.payForParking(self)
            Garage.leaveGarage(self)     
h = Garage(['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5'],['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5'],{'paid':False,'parkingPlaceNumber':'A1'},12)
""" h.takeTicket() """
h.leaveGarage()
""" h.payForParking()  """