from products import Product
from abc import ABC, abstractmethod


class Promotion(ABC):
    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, discount_name: str):
        self.discount_name = discount_name

    def apply_promotion(self, product: Product, quantity) -> float:
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
    def __init__(self, discount_name):
        self.discount_name = discount_name

    def apply_promotion(self, product: Product, quantity) -> float:
        if quantity % 3 == 0:
            promo_coefficient: float = (quantity / 3) * 2  # 3rd item FREE
            total_price = product.price * promo_coefficient
            return total_price
        else:
            promo_coefficient = (quantity % 3) + ((quantity // 3) * 2)
            total_price = product.price * promo_coefficient
            return total_price


class PercentDiscount(Promotion):
    def __init__(self, discount_name, percent):
        self.discount_name = discount_name
        self.percent = percent

    def apply_promotion(self, product: Product, quantity) -> float:
        promo_percentage = self.percent / 100
        total_price = product.price - (product.price * promo_percentage)
        return total_price
