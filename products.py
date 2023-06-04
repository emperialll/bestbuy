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
            self._active = active
        except TypeError:
            print('The value type is not expected.')

    def get_quantity(self) -> int:
        """
        This function return the quantity of certain product
        :return: quantity: int
        """
        return self._quantity

    def set_quantity(self, quantity: int) -> None:
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

    def is_active(self) -> bool:
        """
        This function returns the active status of a certain product
        :return: bool
        """
        return self._active

    def activate(self) -> None:
        """
        This function sets the active value of certain product to True
        :return: None
        """
        self._active = True

    def deactivate(self) -> None:
        """
        This function sets the active value of certain product to False
        :return: None
        """
        self._active = False

    def show(self) -> str:
        """
        This function returns the item name, price and its quantity
        :return: str
        """
        return f'{self.name}, Price: {self.price}, Quantity: {self._quantity}'

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
            if self._quantity >= quantity:
                self.set_quantity(self._quantity - quantity)
                total_price = self.price * quantity
                return total_price
            else:
                # Message for quantity more than available stock
                print("There's no available unit")
                raise ValueError("Insufficient quantity.")
        except TypeError:
            print('Error: Unexpected parameter type: quantity')


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float, active: bool = True):
        super().__init__(name, price, 0, active)

    def show(self):
        """
        This function returns the item name and price
        :return: str
        """
        super().show()
        return f'{self.name}, Price: {self.price}'

    def buy(self, quantity: int) -> float:
        """
        This function gets a quantity of certain product and
        returns the total price.
        :param quantity: int
        :return: total_price: float
        """
        super().buy(quantity)
        try:
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
            total_price = self.price * quantity
            return total_price
        except TypeError:
            print('Error: Unexpected parameter type: quantity')
