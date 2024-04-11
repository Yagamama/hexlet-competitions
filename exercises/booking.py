from datetime import date


# BEGIN (write your solution here)
class Booking:

    def __init__(self):
        self.morning = set()
        self.evening = set()
        self.can_book = True
        self.date1 = None
        self.date2 = None
    
    def book(self, date1, date2):
        self.can_book = True
        #3 return self.valid_date(date1) and self.valid_date(date2) \
        b = False
        if self.is_valid_dates(date1, date2):
            b = self.dates_order().is_empty().booking()
        return b
    
    def is_valid_dates(self, date1, date2):
        try:
            self.date1 = date.fromisoformat(date1)
            self.date2 = date.fromisoformat(date2) 
            return True
        except ValueError:
            print('Dates are wrong!')
            self.date1 = None
            self.date2 = None
            self.can_book = False
            return False
    
    def dates_order(self):
        if self.date1 >= self.date2:
            # print('dates_order = False')
            self.can_book = False
        return self
    
    def is_empty(self):
        if self.can_book:
            #print('is_empty')
            r = (self.date2 - self.date1).days
            d = self.date1
            for _ in range(r):
                if d in self.evening:
                    self.can_book = False
                d = d.replace(day=d.day+1)
                if d in self.morning:
                    self.can_book = False
                # print('item =', d)
        return self
    
    def booking(self):
        if self.can_book:
            # print('booking')
            r = (self.date2 - self.date1).days
            d = self.date1
            for _ in range(r):
                self.evening.add(d)
                d = d.replace(day=d.day+1)
                self.morning.add(d)
            # print('ev = ', list(self.evening))
            # print('mor = ', list(self.morning))
        return self.can_book
# END


if __name__ == '__main__':
    booking = Booking()

    print('res =', not booking.book('2008-11-10', '2008-11-05'))
    print('res = 11.11 - 13.11', booking.book('2008-11-11', '2008-11-13'))
    print('res =', not booking.book('2008-11-12', '2008-11-12'))
    print('res =', not booking.book('2008-11-12', '2008-11-14'))
    print('res = 10.11 - 11.11', booking.book('2008-11-10', '2008-11-11'))
    print('res =', not booking.book('2008-11-12', '2008-11-13'))
    print('res =', not booking.book('2008-11-13', '2008-11-13'))
    print('res = 13.11 - 14.11', booking.book('2008-11-13', '2008-11-14'))
    print('res = 08.05 - 18.05', booking.book('2008-05-08', '2008-05-18'))
    print('res = 09.05 - 10.05', booking.book('2008-05-09', '2008-05-10'))