import promotions
from products import Product
from products import NonStockedProduct
from products import LimitedProduct
from store import Store


# This function displays the main menu
def display_menu():
    """
    This function prints the items of store menu
    :return: None
    """
    print('      Store Menu')
    print('     ------------')
    print('1. List all products in store\n'
          '2. Show total amount in store\n'
          '3. Make an order\n'
          '4. Quit')


# This function prints the list of products
def list_all_products(store_obj):
    """
    This function gets a store object and prints the list of available
    products in the store.
    :param store_obj: Store Object
    :return: None
    """
    product_list = store_obj.get_all_products()
    print('------')
    for item_no, item in enumerate(product_list, start=1):
        print(f'{item_no}. {item.show()}')
    print('------')


# User input function to control the main menu
def get_user_choice():
    """
    This function asks the user to choose his/her preferred option from the
    main menu and enter the relevant number of choice
    :return choice: int
    """
    try:
        choice = int(input('Please choose a number: '))
        return choice
    except ValueError:
        print('Invalid input. Please enter a number.')


# Place order function
def make_order(store_obj):
    """
    This function gets a store object and asks user to input add products and
    relevant quantity to the cart and ultimately place the order. Upon
    successful purchase the total amount paid will be printed.
    :param store_obj: Object
    :return: None
    """
    list_all_products(store_obj)
    print('When you want to finish order, enter empty text.')
    order_items = []
    while True:
        product_id = input('Which product # do you want? ')
        product_quantity = input('What amount do you want? ')
        if not product_id and not product_quantity:
            print('********')
            total_payment = store_obj.order(order_items)
            print(f'Order made! Total payment: ${total_payment}')
            print()
            break
        else:
            try:
                product_index = int(product_id) - 1
                product = store_obj.get_all_products()[product_index]
                quantity = int(product_quantity)
                order_items.append((product, quantity))
                print('Product added to list!')
                print()
            except (ValueError, IndexError):
                print('Invalid input. Please try again.')


# This function executes the main menu for shopping at store
def start(store_obj):
    """
    This function gets a store object and offer multiple options to user for
    shopping at the respective store.
    :param store_obj: object
    :return: None
    """
    while True:
        display_menu()
        user_choice = get_user_choice()
        if user_choice == 1:
            list_all_products(store_obj)
        elif user_choice == 2:
            print(f'Total of {store_obj.get_total_quantity()} items in store.')
            print()
        elif user_choice == 3:
            make_order(store_obj)
        elif user_choice == 4:
            break


# Main program execution section
def main():
    """
    In this section, the main product list is defined
    The new store object is defined
    The start function is called
    :return: None
    """
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2",
                            price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds",
                            price=250, quantity=500),
                    Product("Google Pixel 7",
                            price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250,
                                   maximum=1)
                    ]
    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)  # Define a new store called 'best_buy'
    start(best_buy)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
