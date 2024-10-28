# create the class ItemToPurchase
class ItemToPurchase:
    def __init__(self, item_name='none',item_price=0.0,item_quantity=0,item_description='none'):

        # Initialize the attributes
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Create the function print_item_cost
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')

#Class for shopping cart
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # To add new items
    def add_item(self, item: ItemToPurchase):
        self.cart_items.append(item)

    # To remove an item
    def remove_item(self, item_name: str):
        for i, item in enumerate(self.cart_items):
            if item.item_name == item_name:
                del self.cart_items[i]
                print(f'{item_name} successfully removed!')
                return
        print('Item not found in cart. Nothing removed.')
    
    # To modify/update an item
    def modify_item(self, item: ItemToPurchase):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_description != 'none':
                    cart_item.item_description = item.item_description
                if item.item_price != 0.0:
                    cart_item.item_price = item.item_price
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                print(f'{item.item_name} successfully modified!')
                return
        print('Item not found in cart. Nothing modified.')
    
    # Get the total quantity of all items in the cart
    def get_num_items_in_cart(self):
        total_qty = sum(item.item_quantity for item in self.cart_items)
        return total_qty
    
    # Get the total cost of everything in the cart
    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost
    
    # Outputs the entire shoping cart quantities and cost
    def print_total(self):
        print('\nOUTPUT SHOPPING CART')
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        total_items = self.get_num_items_in_cart()
        print(f'Number of Items: {total_items}')

        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                item_total = item.item_price * item.item_quantity
                print(f'{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${item_total:.2f}')

            total_cost = self.get_cost_of_cart()
            print(f'Total: ${total_cost:.2f}')

    # Outputs all descriptions of items in cart
    def print_descriptions(self):
        print("\nOUTPUT ITEM'S DESCRIPTIONS")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print('Item Descriptions')

        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            for item in self.cart_items:
                print(f'{item.item_name}: {item.item_description}')

# Creates the menu that allows the user to select an option
def print_menu(cart):
    while True:
        print('\nMENU')
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("m - Modify item in cart")
        print("o - Output shopping cart")
        print("d - Display item descriptions")
        print("q - Quit")
        
        # User chooses an option
        choice = input("Choose an option: ")

        # If/else statements for every option
        if choice == 'q':
            print('Quitting...')
            break
        elif choice == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name=item_name, item_price=item_price, item_quantity=item_quantity, item_description=item_description)
            cart.add_item(item)
            print(f"{item_name} added to the cart.")
        elif choice == 'r':
            item_name = input('Enter item name to remove: ')
            cart.remove_item(item_name)
        elif choice == 'm':
            item_name = input('Enter the item name to modify: ')
            item_description = input('Enter the new description (leave blank to not update): ')
            item_price = input('Enter the new price (leave blank to not update): ')
            item_quantity = input('Enter the new quantity (leave blank to not update): ')

            item_description = item_description if item_description else 'none'
            item_price = float(item_price) if item_price else 0.0
            item_quantity = int(item_quantity) if item_quantity else 0

            item = ItemToPurchase(item_name=item_name, item_price=item_price, item_quantity=item_quantity, item_description=item_description)
            cart.modify_item(item)
        elif choice == 'o':
            cart.print_total()
        elif choice == 'd':
            cart.print_descriptions()
            # Error handling
        else:
            print('INVALID CHOICE. Please try again.')

def main():
    customer_name = input('Enter the customer name: ')
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name=customer_name, current_date=current_date)

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    print_menu(cart)


main()