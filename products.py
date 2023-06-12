import promotions


# Class to create different product instances
class Product:
    def __init__(self, name: str, price: float, quantity: int,
                 active: bool = True) -> None:
        """
        Initializer function to be used upon creating any new instance.
        :param name: str - mandatory
        :param price: float - mandatory
        :param quantity: int - mandatory
        :param active: bool - optional -> Default value is True
        """
        if not name:
            raise ValueError("Product name cannot be empty.")

        if price < 0:
            raise ValueError("Product price cannot be negative.")

        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")
        try:
            self.name = name
            self.price = price
            self._quantity = quantity
            self._promotion = None
            self._active = active
        except TypeError:
            print('The value type is not expected.')

    @property
    def quantity(self) -> int:
        """
        This function return the quantity of certain product
        :return: quantity: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        """
        This function sets new quantity of certain product.
        If the updated quantity is ZERO this function toggles the
        Active value to False
        :param quantity: int
        :return: None
        """
        if not isinstance(quantity, int):
            raise TypeError("Invalid quantity type. Expected int.")
        self._quantity = quantity
        if self._quantity == 0:
            self._active = False  # Change active value

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, promotion):
        self._promotion = promotion

    @property
    def active(self) -> bool:
        """
        This function returns the active status of a certain product
        :return: bool
        """
        return self._active

    @active.setter
    def active(self, value: bool) -> None:
        """
        This function sets the active value of certain product to True
        :return: None
        """
        self._active = value

    def deactivate(self) -> None:
        """
        This function sets the active value of certain product to False
        :return: None
        """
        self._active = False

    def __str__(self) -> str:
        """
        This function returns the item name, price and its quantity
        :return: str
        """
        if isinstance(self.promotion, promotions.Promotion):
            return f'{self.name}, Price: {self.price}, ' \
                   f'Quantity: {self.quantity}, ' \
                   f'Promotion: {self.promotion.discount_name}'
        else:
            return f'{self.name}, Price: {self.price}, ' \
                   f'Quantity: {self.quantity}'

    def __gt__(self, other_product):
        return self.price > other_product.price

    def __lt__(self, other_product):
        return self.price < other_product.price

    def __eq__(self, other_product):
        return self.price == other_product.price

    def buy(self, quantity: int) -> float:
        """
        This function gets a quantity of certain product and
        returns the total price.
        :param quantity: int
        :return: total_price: float
        """
        if not isinstance(quantity, int):
            raise TypeError("Invalid quantity type. Expected int.")
        try:
            if self.quantity >= quantity:
                if isinstance(self.promotion, promotions.Promotion):
                    total_price = self.promotion.apply_promotion(self,
                                                                 quantity)
                else:
                    total_price = self.price * quantity
                self.quantity = self.quantity - quantity
                return total_price
            else:
                # Message for quantity more than available stock
                print("There's no available unit")
                raise ValueError("Insufficient quantity.")
        except TypeError:
            print('Error: Unexpected parameter type: quantity')


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float,
                 active: bool = True):
        super().__init__(name, price, 0, active)
        self._promotion = None

    def show(self):
        """
        This function returns the item name and price
        :return: str
        """
        super().__str__()
        return f'{self.name}, Price: {self.price}, ' \
               f'Promotion: {self.promotion.discount_name}'

    def buy(self, quantity: int) -> float:
        """
        This function gets a quantity of certain product and
        returns the total price.
        :param quantity: int
        :return: total_price: float
        """
        try:
            if isinstance(self.promotion, promotions.Promotion):
                total_price = self.promotion.apply_promotion(self, quantity)
            else:
                total_price = self.price * quantity
            return total_price
        except TypeError:
            print('Error: Unexpected parameter type: quantity')


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int,
                 maximum: int = 1, active: bool = True):
        super().__init__(name, price, quantity, active)
        self.maximum = maximum

    def buy(self, quantity: int = 1) -> float:
        """
        This function gets a quantity of certain product and
        returns the total price.
        :param: quantity: int
        :return: total_price: float
        """
        quantity = self.maximum
        try:
            if self.quantity >= quantity:
                self.quantity = self.quantity - quantity
                total_price = self.price * quantity
                return total_price
            else:
                # Message for quantity more than available stock
                print("There's no available unit")
                raise ValueError("Insufficient quantity.")
        except TypeError:
            print('Error: Unexpected parameter type: quantity')
