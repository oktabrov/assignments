class SupplyError(Exception):
    pass


class IngredientNotFoundError(SupplyError):
    def __init__(self, ingredient_name):
        self.ingredient_name = ingredient_name
        super().__init__(f"ingredient not found: {ingredient_name}")


class InsufficientIngredientError (SupplyError):
    def __init__(self, ingredient_name, requested, available):
        self.ingredient_name = ingredient_name
        self.requested = requested
        self.available = available
        self.shortage = requested - available
        super().__init__(f"cannot use {requested} of {ingredient_name}: only {available} in stock, short by {self.shortage}")


class InvalidQuantityError(SupplyError):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"invalid quantity: {quantity}. must be positive")


class Restaurant:
    def __init__(self):
        self.ingredients = dict()

    def add_ingredient(self, name, cost, quantity):
        if quantity<=0:
            raise InvalidQuantityError(quantity)
        if name in self.ingredients:
            self.ingredients[name]['quantity'] += quantity
            self.ingredients[name]['cost'] = cost
        else:
            self.ingredients[name] = {'cost': cost, 'quantity': quantity}

    def use(self, name, quantity):
        if quantity<=0:
            raise InvalidQuantityError(quantity)
        try:
            available = self.ingredients[name]['quantity']
        except KeyError:
            raise IngredientNotFoundError(name) from None
        if available < quantity:
            raise InsufficientIngredientError(name, quantity, available)
        self.ingredients[name]['quantity'] -= quantity
        return round(quantity * self.ingredients[name]['cost'], 2)
    
    def total_value(self):
        return round(sum(self.ingredients[name]['cost'] * self.ingredients[name]['quantity'] for name in self.ingredients.keys()), 2)