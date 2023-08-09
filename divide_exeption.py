# A function that returns division with exception
def division(a, b):
    return a / b


try:
    ans = division(5, 0)
except Exception:
   print('sorry, can not be divided br zero')

division(25, 8)
   
