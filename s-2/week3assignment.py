class OfficeSupply:
    def __init__(self, item_name, price_per_box, box_count):
        self.item_name = item_name
        self.price_per_box = price_per_box
        self.box_count = box_count
        
    def __str__(self):
        return f"{self.item_name}: {self.box_count} box(es) at ${self.price_per_box}"
    
    def __repr__(self):
        return f"OfficeSupply('{self.item_name}', {self.price_per_box}, {self.box_count})"
    
    def __add__(self, other):
        if isinstance(other, OfficeSupply):
            if self.item_name == other.item_name:
                return OfficeSupply(self.item_name, self.price_per_box, self.box_count+other.box_count)
            else:
                return NotImplemented
        elif isinstance(other, int):
            return OfficeSupply(self.item_name, self.price_per_box, self.box_count+other)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, OfficeSupply):
            return True if self.item_name == other.item_name and self.price_per_box == other.price_per_box else NotImplemented
        return NotImplemented
    
    def __bool__(self):
        return self.box_count > 0
supply1 = OfficeSupply("Printer Paper", 25.0, 5)
supply2 = OfficeSupply("Printer Paper", 25.0, 3)
supply3 = OfficeSupply("Stapler", 12.5, 0)

print(str(supply1))
print(repr(supply1))
print(supply1 + supply2)
print(supply1 + 2)
print(supply1 == supply2)
print(bool(supply1))
print(bool(supply3))