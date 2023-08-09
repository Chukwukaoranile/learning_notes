'''
def tax(*args):
    income = 1300 
    rate = 10
    calc_tax = income * rate / 100
    print('Tax is ', calc_tax)

tax(1700, 10)
'''
menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
    }

def calculate_subtotal(**kwargs):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME]
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = 0
    for bill_record, bill_counter in kwargs:
        bill_counter += bill_counter
    return round(subtotal, 2)
    print(subtotal, kwargs)
print(calculate_subtotal(cake=123, tea=432))
calculate_subtotal()



