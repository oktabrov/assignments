def log_operation(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if value:
            print(f"[OK] {func.__name__} successful")
        else:
            print(f"[FAIL] {func.__name__} denied")
    return wrapper
class Show:
    _schedule = []
    def __init__(self, title, total_seats):
        self.title = title
        self.total_seats = total_seats
        self._sold = 0
        Show._schedule.append(self)
    @log_operation
    def sell_ticket(self):
        if self._sold == self.total_seats:
            return False
        else:
            self._sold += 1
            return True
    @log_operation
    def refund_ticket(self):
        if self._sold == 0: return False
        else:
            self._sold -= 1
            return True
    def seats_left(self):
        return self.total_seats - self._sold
    def sold_percent(self):
        return round(self._sold/self.total_seats*100, 1)
    @classmethod
    def from_schedule(cls, entry):
        title, seats = entry.split(':')
        return cls(title, int(seats))
    @staticmethod
    def is_valid_booking(code):
        return len(code) == 13 and code.isdigit()
    @classmethod
    def total_seats_left(cls):
        unsold = 0
        for i in cls._schedule:
            unsold += i.seats_left()
        return unsold
s1 = Show("Romeo and Juliet", 2)
s2 = Show.from_schedule("Hamlet:3")

s1.sell_ticket()
s1.sell_ticket()
s1.sell_ticket()
s1.refund_ticket()

s2.sell_ticket()
s2.refund_ticket()
s2.refund_ticket()

print(f"{s1.title}: seats left = {s1.seats_left()}, sold = {s1.sold_percent()}%")
print(f"{s2.title}: seats left = {s2.seats_left()}, sold = {s2.sold_percent()}%")

print(f"Valid booking '4567890123456': {Show.is_valid_booking('4567890123456')}")
print(f"Valid booking '456-789': {Show.is_valid_booking('456-789')}")
print(f"Total seats left: {Show.total_seats_left()}")