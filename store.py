# Class to create different store instances
class Store:
    def __init__(self, product):
        """
        Initializer function to be used upon creating any new instance.
        :param product: list of product objects - Mandatory
        """
        self.product = product

    def add_product(self, product) -> None:
        """
        This function gets a product object and add it to the product list
        :param product: object
        :return: None
        """
        self.product.append(product)

    def remove_product(self, product) -> None:
        """
        This function gets a product object and remove it
        from the product list
        :param product: object
        :return: None
        """
        self.product.remove(product)

    def get_total_quantity(self) -> int:
        """
        This function returns the total quantity of all
        available items in store
        :return: total_quantity: int
        """
        total_quantity: int = 0
        for item in self.product:
            total_quantity += item.get_quantity()
        return total_quantity

    def get_all_products(self) -> list:
        """
        This function returns a list of active products in store
        :return: product_list: list
        """
        product_list = []
        for item in self.product:
            if item.is_active:  # filter out the inactive products
                product_list.append(item)
        return product_list

    @staticmethod
    def order(shopping_list) -> float:
        """
        This function gets a list of products as a shopping list and returns
        the total price each product item in the shopping list is a tuple of
        product object and shopping quantity
        :param shopping_list: list
        :return: total_price: float
        """
        total_price: float = 0
        for item in shopping_list:
            total_price += item[0].buy(item[1])
        return total_price
