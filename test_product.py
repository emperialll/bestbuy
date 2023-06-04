import pytest
from products import Product


def test_create_product():
    # Create a product
    product = Product("Example Product", 10.99, 5)

    # Check if the product is created correctly
    assert product.name == "Example Product", "Incorrect product name"
    assert product.price == 10.99, "Incorrect product price"
    assert product.get_quantity() == 5, "Incorrect product quantity"
    assert product.is_active() is True, "Product should be active"

    # Check the output of the show() method
    expected_output = "Example Product, Price: 10.99, Quantity: 5"
    assert product.show() == expected_output, "Incorrect show() output"

    # Check purchasing quantity is lower or equal than available items in stock
    with pytest.raises(ValueError):
        product.buy(6)

    # Check buying functionality
    assert product.buy(2) == 21.98, "Incorrect total price"
    assert product.get_quantity() == 3, "Incorrect quantity after buying"

    # Check setting quantity to zero deactivates the product
    product.set_quantity(0)
    assert product.is_active() is False, "Product should be deactivated"

    # Check activating and deactivating the product
    product.activate()
    assert product.is_active() is True, "Product should be activated"
    product.deactivate()
    assert product.is_active() is False, "Product should be deactivated"

    # Check handling unexpected parameter type when buying
    with pytest.raises(TypeError):
        product.buy("invalid")

    # Check buying more than available stock
    with pytest.raises(ValueError):
        product.buy(5)

    # Check handling unexpected parameter type when setting quantity
    with pytest.raises(TypeError):
        product.set_quantity("invalid")

    print("Product creation test passed successfully.")


def test_create_product_with_invalid_details():
    # Test empty name
    with pytest.raises(ValueError):
        Product("", 10.99, 5)

    # Test negative price
    with pytest.raises(ValueError):
        Product("Example Product", -10.99, 5)

    # Test negative quantity
    with pytest.raises(ValueError):
        Product("Example Product", 10.99, -5)

    print("Invalid product details test passed successfully.")
