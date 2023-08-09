**Handling exception**
This allows the your program to run without crashing when encountered with error(Example ZeroDivisionError)
if you want to achieve this, simple add the lines of code that produces the error to "try" and "except"
ex: below code will produce ZeroDivisionError, adding same to try and except will help the code not to crash and continue running

	print(10 / 0)

_Adding same to try and except will help the code not to crash and continue running_

```
try:
    print(10 / 0)
except:
    print('Can not be divided by zero')
**Ex 2: In math there are rules about dividing by zero. The below code is trying to do just that and will throw a ZeroDivisionError. Add exception handling to return back 0 instead of allowing the error to be thrown.**

```
def divide_by(a, b):
    return a / b


ans = divide_by(40, 0)
print(ans)

```

**Solution**

```
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except:
    print('return back 0')
```

**ex 3:  FileNotFoundError. The code below is looking for a file that does not exist. Add exception handling to catch this error and return the following "The file could not be found".**

```
with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())
```

**Solution**
```
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print('The file could not be found')
```

### All the above exceptions will take care of all exceptions. But it best practice to specify your exception

Specifying exception in the above ZeroDivisionError


```
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except ZeroDivisionError as e:
    print('return back 0', e)
```
This will make the code to catch only ZeroDivisionError

**Handling multiple errors**

**Ex 4**
```
values = [10, 5, 6, 0, 9, 8, 2]

for val in values:
    try:
        print(int("Hello"))
    except ValueError as e:
        print(str(e))
    except ZeroDivisionError as e:
        pass
```
The above code will catch exception for both VAlueError and ZeroDivisionError. The ValueError exceprion will print the exception class due to the print function. while the ZeroDivisionError exception will pass without printing anything. if two exception has one requirement, they can be compined in one block. eg.
```
values = [10, 5, 6, 0, 9, 8, 2]

for val in values:
    try:
        print(int("Hello"))
    except ValueError as e:
        print(str(e))
    except (ZeroDivisionError, AttributeError) as e:
        pass
```

"except Exception as e:" can be used to catch all the exceptions but is not best practice. it's always adviced to specify the exception.

**Raise Excetion allows the code to crash but maybe help the developer to displays information about the crash to the user.
**ex 5**

```
values = [10, 5, 6, 0, 9, 8, 2]

for val in values:
    try:
        print(int(10 / int(val))
    except ZeroDivisionError as e:
        pass
    except ValueError as e:
        raise
```

The above code will raise ValueError

