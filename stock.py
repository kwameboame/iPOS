import datetime as dt

# Sample data
products = [
    {
        'id': 1,
        'name': 'Paracetamol',
        'stock': 100,
        'expiry': dt.datetime(2019, 12, 25),
        'minimum_stock': 10,
        'price': 5.00,
        'cost': 3.50
    },
    {
        'id': 2,
        'name': 'Gebedol',
        'stock': 100,
        'expiry': dt.datetime(2019, 10, 25),
        'minimum_stock': 10,
        'price': 10.00
    },
]

total_sales = 0
sales = []


def expired(item):
    date = item['expiry']  # get item expiry date
    today = dt.datetime.today()  # get today's date
    days_to_expiry = (date.date() - today.date()).days  # Days left to expiry

    # Check if expiry date has been reached
    if days_to_expiry < 1:
        print("This product has expired")
        return True

    # if item expires within 30 days, print this warning
    elif days_to_expiry in range(1, 31):
        print("This item is expiring soon")

    else:
        pass


def order(item):
    global total_sales

    # print item info for cashier
    print('\nItem is {}.\nCurrent stock is {}.\nPrice is {}'
          '\n\n'.format(item['name'], item['stock'], item['price']))

    get_qty = input('What many do you want? ')  # Get purchase quantity

    # See if there is enough stock for the quantity demanded and run the order
    if int(get_qty) <= item['stock']:
        new_stock = item['stock'] - int(get_qty)
        item['stock'] = new_stock
        cash_received = input('Cash taken: ')
        change = float(cash_received) - (item['price'] * int(get_qty))
        sales = (int(get_qty) * item['price'])
        total_sales += sales

        print('\nTotal sales for {} is {}.\nNew stock is {}.\nChange is {}'
              '\n\n'.format(item['name'], total_sales, item['stock'], change))

        if item['stock'] > item['minimum_stock']:
            pass

        elif item['stock'] == 0:
            print('Item is out of stock \n')

        else:
            print("WARNING! Item stock is below threshold \n")

    # If item is out of stock, say so
    elif item['stock'] == 0:
        print('\nItem is out of stock \n')

    # quantity selected is more so print out current stock
    else:
        print('Quantity selected is more than item in stock. You can only'
              ' sell {} items \n'.format(item['stock']))


# Run the code with the data sample
if __name__ == '__main__':
    # If product has not expired, process order
    while True:
        if expired(products[0]) is True:
            break
        else:
            order(products[0])
