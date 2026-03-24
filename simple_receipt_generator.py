def positive_quantity(prompt):

    while True:
        number = input(prompt)

        if number == '':
            print('Number cannot be blank. Enter a whole number: ')
        elif not number.isdigit():
            print('Please enter a number: ')
        else:
            number = int(number)

            if number <= 0:
                print('Number must be greater than 0: ')
            else:
                return number

def positive_price(prompt):

    while True:
        number = input(prompt)
        parts = number.split('.')

        if number == '':
            print('Number cannot be blank. Enter a number.')
        elif number.count('.') > 1:
            print('Only one decimal point allowed.')
        elif not number.replace('.', '', 1).isdigit():
            print('Please enter a valid number.')
        elif '.' in number and len(parts[1]) > 2:
            print('Only two digits allowed after decimal point.')
        else:
            number = float(number)

            if number <= 0:
                print('Number must be greater than 0: ')
            else:
                return number

item_list = []

running = True

while running:

    item_name = input('Enter item name: ').strip().capitalize()
    item_price = positive_price('Enter item price: ')
    item_quantity = positive_quantity('Enter item quantity: ')

    item = {
        'name': item_name,
        'quantity': item_quantity,
        'price': item_price,
        'total_cost': item_quantity * item_price
    }

    item_list.append(item)

    while True:

        another = input('Add another item? (Y/N): ').strip().upper()

        if another == 'Y':
            break
        elif another == 'N':
            running = False
            break
        else:
            print('Invalid input. Enter Y or N.')

print('Simple Receipt Generator')
print()

grand_total = 0

for item in item_list:
    print(f'Name: {item["name"]}')
    print(f'Quantity: {item["quantity"]}')
    print(f'Price: ${item["price"]:.2f}')
    print(f'Subtotal: ${item["total_cost"]:.2f}')
    print()

    grand_total += item['total_cost']

print(f'Grand Total: ${grand_total:.2f}')