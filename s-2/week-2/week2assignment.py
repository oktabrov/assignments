class Flight:
    def __init__(self, flight_number, total_seats, booked_seats = 0):
        self._flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = booked_seats
    @property
    def flight_number(self):
        return self._flight_number
    @property
    def total_seats(self):
        return self._total_seats
    @total_seats.setter
    def total_seats(self, value):
        if value < 1:
            raise ValueError("Total seats must be at least 1")
        self._total_seats = value
    @property
    def booked_seats(self):
        return self._booked_seats
    @booked_seats.setter
    def booked_seats(self, value):
        if value < 0:
            raise ValueError("Booked seats cannot be negative")
        elif value > self._total_seats:
            raise ValueError("Booked seats cannot exceed total seats")
        self._booked_seats = value
    @property
    def open_seats(self):
        return self._total_seats - self._booked_seats
    @property
    def booking_rate(self):
        return round((self._booked_seats / self._total_seats)*100, 1)
    def book(self, tickets):
        if tickets < 0: 
            raise ValueError("Number of tickets must be positive")
        elif tickets > self._total_seats - self._booked_seats:
            raise ValueError("Not enough open seats")
        self._booked_seats += tickets
    def cancel(self, tickets):
        if tickets < 0: 
            raise ValueError("Number of tickets must be positive")
        elif tickets > self._booked_seats:
            raise ValueError("Cannot cancel more than booked")
        self._booked_seats -= tickets
f = Flight("UZ-101", 180)
print(f.flight_number, f.open_seats, f.booking_rate)

f.book(120)
print(f.booked_seats, f.booking_rate)

f.cancel(30)
print(f.open_seats)

try:
    f.book(100)
except ValueError as e:
    print(e)

try:
    f.flight_number = "X"
except AttributeError:
    print("Cannot change flight number")