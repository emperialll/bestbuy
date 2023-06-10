from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, discount_name: str):
        self.discount_name = discount_name

    def apply_promotion(self, product, quantity) -> float:
        if quantity % 2 == 0:
            promo_coefficient: float = \
                (quantity / 2) * 1.5  # 2nd item half price
            total_price = product.price * promo_coefficient
            return total_price
        else:
            promo_coefficient = 1 + ((quantity // 2) * 1.5)
            total_price = product.price * promo_coefficient
            return total_price


class ThirdOneFree(Promotion):
    """
    A promotion that offers the third item for free when purchasing multiple
    items.

    This promotion calculates the total price for a given quantity of
    a product based on the "third one free" offer. If the quantity is a
    multiple of 3, the price is calculated by applying a coefficient of
    (quantity / 3) * 2, effectively making every third item free.
    If the quantity is not a multiple of 3, the price is calculated by
    applying a coefficient of (quantity % 3) + ((quantity // 3) * 2),
    where the remainder is multiplied by the product's price and added to the
    price of the multiples of 3.

    Args:
        discount_name (str): The name of the discount associated with the
        promotion.

    Methods:
        apply_promotion(product: Product, quantity) -> float:
            Apply the "third one free" promotion to the given product and
            quantity, and return the total price.

    Attributes:
        discount_name (str): The name of the discount associated with the
        promotion.
        """
    def __init__(self, discount_name):
        """
        Initialize the ThirdOneFree promotion.

        Args:
            discount_name (str): The name of the discount associated with the
            promotion.
        """
        self.discount_name = discount_name

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the "third one free" promotion to the given product and quantity,
        and return the total price.

        If the quantity is a multiple of 3, the price is calculated by applying
         a coefficient of (quantity / 3) * 2, effectively making every third
         item free. If the quantity is not a multiple of 3, the price is
         calculated by applying a coefficient of (quantity % 3) +
         ((quantity // 3) * 2), where the remainder is multiplied by the
         product's price and added to the price of the multiples of 3.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        if quantity % 3 == 0:
            promo_coefficient: float = (quantity / 3) * 2  # 3rd item FREE
            total_price = product.price * promo_coefficient
            return total_price
        else:
            promo_coefficient = (quantity % 3) + ((quantity // 3) * 2)
            total_price = product.price * promo_coefficient
            return total_price


class PercentDiscount(Promotion):
    """
    A promotion that applies a percentage discount to the price of a product.

    This promotion calculates the total price for a given product and quantity
     by applying a percentage discount to the original price. The discount is
     determined by the provided percentage value.

    Args:
        discount_name (str): The name of the discount associated with the
        promotion.
        percent (float): The percentage value of the discount to be applied.

    Methods:
        apply_promotion(product: Product, quantity) -> float:
        Apply the percentage discount to the given product and quantity,
        and return the discounted total price.

    Attributes:
        discount_name (str): The name of the discount associated with the
        promotion.
        percent (float): The percentage value of the discount to be applied.
    """
    def __init__(self, discount_name, percent):
        """
        Initialize the PercentDiscount promotion.

        Args:
           discount_name (str): The name of the discount associated with the
           promotion.
           percent (float): The percentage value of the discount to be applied.
        """
        self.discount_name = discount_name
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply the percentage discount to the given product and quantity, and
        return the discounted total price.

        The total price is calculated by subtracting the discounted amount
        from the original price, where the discounted
        amount is determined by multiplying the product's price by the
        percentage discount value.

        Args:
           product (Product): The product to apply the promotion to.
           quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the percentage discount.
        """
        promo_percentage = self.percent / 100
        total_price = product.price - (product.price * promo_percentage)
        return total_price
