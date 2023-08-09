# A python code that accepts float input.

x = float(input('Kindly Enter a Number: '))


if x < 50:
    print('First Suite')
    print('x is small')

elif x > 50:
    print('second Suite')
    print('x is large')
    if x == 60:
        print('x is large by 10pcs')
else:
    print('x is neutral')
