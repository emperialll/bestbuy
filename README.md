# My Python Store Management Project

Welcome to my Python Store Management Project! This project has been implemented as a basic showcase of objected-oriented programming in Python. This README provides an overview of the project's structure, functionality, and how to get started.

## Table of Contents

1. [Project Overview](#project-overview)
2. [File Structure](#file-structure)
3. [Usage](#usage)
4. [Testing](#testing)
5. [Contributing](#contributing)

## Project Overview

The project consists of several Python files that work together to create a store management system. Here's a brief overview of the main components:

- **`main.py`**: The entry point of the application, which presents a menu for users to interact with the store.

- **`product.py`**: Defines the `Product` class and its subclasses, which represent products and their properties, such as name, price, quantity, and promotions.

- **`promotions.py`**: Contains promotion classes and logic that can be associated with products to apply discounts.

- **`store.py`**: Defines the `Store` class, which represents a store and provides methods to manage products, calculate the total quantity, and place orders.

- **`test_product.py`**: Includes test cases for the `Product` class, covering various aspects of product creation and functionality.

## File Structure

Here's a breakdown of the project's file structure:

- `main.py`: The main entry point for the store management application.
- `product.py`: Defines the `Product` class and its subclasses.
- `promotions.py`: Contains promotion classes and logic.
- `store.py`: Defines the `Store` class for managing products.
- `test_product.py`: Test cases for the `Product` class.

## Usage

To run the store management application, you can execute the `main.py` script:

```shell
python main.py
```

This will start the interactive store interface, allowing you to list products, view the total quantity, make orders, and more.

Please note that this project assumes Python 3 is installed on your system.

## Testing

To ensure the functionality and correctness of the Product class, you can run the test suite provided in **`test_product.py`** using the **`pytest`** framework. Make sure you have **`pytest`** installed:

```shell
pip install pytest
```

Then, run the tests:

```shell
pytest test_product.py
```

This will execute the test cases and verify that the Product class behaves as expected.

## Contributing

If you'd like to contribute to this project or report any issues, please feel free to open an issue or submit a pull request on the project's GitHub repository.

Happy store management and OOP with Python!
