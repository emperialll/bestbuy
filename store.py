# Class to create different store instances
class Store:
    def __init__(self, product):
        """
        Initializer function to be used upon creating any new instance.
        :param product: list of product objects - Mandatory
        """
        self.product = product

    def __contains__(self, product_name):
        """
            Check if a product with the given name exists in the store.
            Args:
                product_name (str): The name of the product to check.
            Returns:
                bool: True if a product with the given name exists in the
                store, False otherwise.
        """
        return product_name in self.get_all_products()

    def __add__(self, other_store):
        """
            Merge the products of two stores and create a new store.
            Args:
                other_store (Store): The other store whose products should be
                merged with the current store.
            Returns:
                Store: A new store containing the merged products from both
                stores.
        """
        new_store = Store([])
        all_items = list(self.product) + list(other_store.product)
        for item in all_items:
            new_store.add_product(item)
        return new_store

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
            total_quantity += item.quantity
        return total_quantity

    def get_all_products(self) -> list:
        """
        This function returns a list of active products in store
        :return: product_list: list
        """
        product_list = []
        for item in self.product:
            if item.active:  # filter out the inactive products
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
