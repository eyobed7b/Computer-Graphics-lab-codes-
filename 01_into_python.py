'''
What is Python?
According to Me (Eyob), Python is just a pseudo code but a programming language. :)
I'm not kidding. If you didn't believe me, see the following codes...
'''

'''-------------------------OutPut-------------------------'''

print('hello world')

# print("hello world but in double quote")

# print("If you are addicted to semi-colon");

# print('''
# If you have a long multiline 
# string encompass 
# them in 3 quotes.
# ''');

# print('"hello world"')              # Output: "hello world"

# print("'hello world'")              # Output: 'hello world'

''' Escaped Sequence '''
# print('\'hello world\'')            # Output: 'hello world'    

# print("\"hello world\"")            # Output: "hello world" 

# print('It\'s python')               # Output: "It's python" 

# print('\t I am indented, and \nI am in new line')   # Output:    I am indented, and 
#                                                     #         I am in new line" 

''' Concatenation '''
# print('hello' + '   ' + 'world')        # Output: hello   world 

# print('String with number', 3)          # Output: String with number 3        #you can't concatenate with + sign, this will work only if both are strings
# print('String with boolean?', True)     # Output: String with boolean? True

# print(f'Your age is {20}')              # Output: Your age is 20         #f is for formated string
# print(f'It is {False}')                 # Output: It is False

# print('Your name is {} your age is {} it is {}'.format('ABC', 18, True))        # Output: Your name is ABC your age is 18 it is True
# print('Your name is {2} your age is {1} it is {0}'.format(False, 22, 'DEF'))    # Output: Your name is DEF your age is 22 it is False


'''-------------------------Data types-------------------------'''
''' int, float, bool, str, list, tuple, set, dict, **complex '''
# print(type(2))          # Output: <class 'int'>
# print(type(2.1))        # Output: <class 'float'>
# print(type(True))       # Output: <class 'bool'>
# print(type('HI'))       # Output: <class 'str'>
# print(type([11, 16, 'a', True, 'abc']))       # Output: <class 'list'>
# print(type((1,2)))                            # Output: <class 'tuple'>
# print(type({'id': 804, 'name': 'ABC'}))       # Output: <class 'dict'>


''' type casting
    eg: str(100) => now 100 is '100' 
'''     
# print(str(100) + ' sss')    # Output: 100 sss
# print(type(str(100)))       # Output: <class 'str'>

# print(12 + float('3.14'))   # Output: 15.14

# print(bool(0))              # Output: False   #Only integer 0 will be boolean false after casting  
# print(bool('0'))            # Output: True
# print(bool('True'))         # Output: True
# print(bool('false'))        # Output: True
# print(bool('abc'))          # Output: True
# print(bool(1))              # Output: True
# print(bool(23))             # Output: True
# print(bool(-1))             # Output: True

# print(bin(7))               # Output: 0b111
# print(oct(345))             # Output: 0o531
# print(hex(255))             # Output: 0xff
# print(int('0b111',2))       # Output: 7
# print(int('0o531',8))       # Output: 345
# print(int('0xff',16))       # Output: 255

'''-------------------------Math-------------------------'''
# print(2 + 1 * 9)        # Output: 11
# print(2 * 3)            # Output: 6
# print(2 ** 3)           # Output: 8         # 2 the power of 3
# print(6 / 2)            # Output: 3
# print(5 // 3)           # Output: 1         # devision result but rounded to integer
# print(5 % 3)            # Output: 2         # modulo (remainder)

# print(round(6.12556))       # Output: 2
# print(round(6.12556, 2))    # Output: 6.13
# print(abs(-6))              # Output: 6
# print(min(12,14,7,56,4))    # Output: 4
# print(max(12,14,7,56,4))    # Output: 56
# print(pow(2,3))             # Output: 8

'''
To use the below math methods you have to import 'math' library
        To import any library you can use:
           from [library_name] import *
                       OR
            import [library_name]   => but you need to use the [library_name]  before the methods [ eg: [library_name].method_name() ]
                       OR
            import [library_name] as [alias_name]   => but you need to use this alias before the methods [ eg: [alias_name].method_name() ] 
'''
# from math import *


# print(fabs(-77))          # Output: 77.0    # returns the absolute value of the number
# print(fmod(5,2))          # Output: 1.0     # returns the reminder when x is divide by y

# print(ceil(6.12556))      # Output: 7       # returns the nearest integer greater than the number
# print(floor(6.12556))     # Output: 6       # returns the largest integer lessthan or equal to the number
# print(trunc(8.78))        # Output: 8       # returns the truncates value of the real number to the nearest integral toward 0.

# print(factorial(4))       # Output: 24      # returns the factorial of the number

# print(exp(2))             # Output: 7.38905609893065        # returns e**x
# print(log(8))             # Output: 2.0794415416798357      # returns log of the number to the base e
# print(log(8,2))           # Output: 3.0                     # returns log of the number to the base

# x = nan
# print(isnan(x))         # Output: True      # returns true if the variable is NaN (Not a Number)

# x = 12
# print(isnan(x))         # Output: False

# x2 = float('nan')
# print(isnan(x2))        # Output: True

# print(sqrt(4))          # Output: 2.0                       # returns the square root of the number
# print(sin(45))          # Output: 0.8509035245341184        # returns the sine of the number
# print(cos(45))          # Output: 0.5253219888177297        # returns the cosine of the number
# print(tan(45))          # Output: 1.6197751905438615        # returns the tangent of the number
# print(cosh(45))         # Output: 1.7467135528742547e+19    # returns the hyperbolic sine of the number
# print(cos(45))          # Output: 0.5253219888177297        # returns the inverse hyperbolic sine of the number

# print(degrees(60))      # Output: 3437.746770784939         # converts angle x from radians to degree
# print(radians(3437.75)) # Output: 60.00005636043507         # converts angle x from degree to radians

'''---------------------------Logical & Membership Operators---------------------------'''
# print((10 != 11) and False)         # Output: False
# print(True or (10 > 100))           # Output: True
# print(not False)                    # Output: True

''' Membership Operators ('is' & 'is not') can be used for literals '''
# i = 10; j = 10; k = 40; l1 = 'abc'; l2 = 'cde'
# print(i is j)                       # Output: True
# print(l1 is l2)                     # Output: False
# print(i is not k)                   # Output: True

'''---------------------------String---------------------------'''
# name = 'ABC DEF'
# print(name[0])          #Output: A
# print(name[1:])         #Output: BC DEF
# print(name[:5])         #Output: ABC D
# print(name[1:5])        #Output: BC D
# print(name[0:5:2])      #Output: ACD
# print(name[::2])        #Output: ACDF
# print(name[-1])         #Output: F
# print(name[-5:-1])      #Output: C DE
# print(name[-1:-5])      #Output: no output
# print(name[::-1])       #Output: reverse order

# myText = 'my random text here.'
# print(len(myText))                          #Output:  20                             Length of your text
# print(myText.capitalize())                  #Output:  My random text here.           Capitalizes the first word
# print(myText.lower())                       #Output:  my random text here.           Converts all texts to lower case
# print(myText.upper())                       #Output:  MY RANDOM TEXT HERE.           Converts all texts to upper case
# print(myText.find('ran'))                   #Output:  3                              Search for the specified string index
# print(myText.replace('text', 'string'))     #Output:  my random string here.         Search for the first string and replace by the second one


'''-------------------------User Input-------------------------'''
# name = input('What is your name?\n')
# print('Welcome ' + name)

# x = input('Enter the first number\n')
# y = input('Enter the second number\n')
# sum = float(x) + float(y)
# print("the sum is" , sum);

# yearOfBirth = input('Enter your year of birth?\n')
# age = 2021 - int(yearOfBirth)
# print('Your age is' , age)

'''-------------------Lists-----------------------'''
# myList = [15, 22, 53, 11]
# print(myList[0])                              # Output: 15
# print(myList[1])                              # Output: 22
# print(myList[2])                              # Output: 53
# print(myList[3])                              # Output: 11

# myRandom = ['a', 785, 'abc', True]
# print(myRandom)                             # Output: ['a', 785, 'abc', True]
# print(myRandom[0:3])                        # Output: ['a', 785, 'abc']
# print(myRandom[0:3:1])                      # Output: ['a', 785, 'abc']
# print(myRandom[::2])                        # Output: ['a', 'abc']        

# myAlpha = ['a', 'b', 'c']
# myAlpha[0] = 'z'
# print(myAlpha)                            # Output: ['z', 'b', 'c']

# myNum = [10, 20, 30, 40, 50]
# myNewNum = myNum[1:5]
# print(myNewNum)                           # Output: [20, 30, 40, 50]

# myLetter = ['b', 'c']
# print(myLetter)                     # Output: ['b', 'c']
# myLetter.append('d')
# print(myLetter)                     # Output: ['b', 'c', 'd']
# myLetter.insert(0, 'a')
# print(myLetter)                     # Output: ['a', 'b', 'c', 'd']
# myLetter.extend(['e', 'f', 'g'])
# print(myLetter)                     # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(myLetter.index('e'))          # Output: 4
# myLetter.remove('f')    
# print(myLetter)                     # Output: ['a', 'b', 'c', 'd', 'e', 'g']
# myLetter.pop(0)
# print(myLetter)                     # Output: ['b', 'c', 'd', 'e', 'g']
# myLetter[:] = 'k'
# print(myLetter)                     # Output: ['k']


'''-------------------Conditional Statements & Conditional expressions-----------------------'''
'''
    No switch case in Python
'''
# x = -5
# if x < 0:
#     x *= -1 
# print('Absolute value = ', x)         # Output: 5       


# k = 70
# if k >= 50:
#     print('Pass')
# else:
#     print('Fail')                     # Output: Pass

# n = -70
# if n > 0:
#     print('Positive')
# elif n < 0:
#     print('Negative')
# else:
#     print('Zero')                     # Output: Negative

# a = 10
# b = 50
# min = a if a < b else b 
# print(min)                              #10             

# a = 10
# b = 50
# min = a < b and a or b 
# print(min)                            #10 

# a = 10
# b = 50
# print((b, a) [a < b])                         #10
# print({True: a, False: b} [a < b])            #10
# print((lambda: b, lambda: a)[a < b]())        #10

'''-------------------Loops-----------------------'''
'''
    No for-loop & do-while loop in Python, only while & for-each are there
'''
# n = 0
# while n <= 5:
#     n += 1
#     print(n)                  # Output: 1 2 3 4 5 6

# n = 0
# while n <= 5:
#     n += 1
#     print(n)
# else:
#     print("Done")               # Output: 1 2 3 4 5 6 Done

# n = 0
# while n <= 5:
#     n += 1
#     if n == 2:
#         continue
#     print(n)                      # Output: 1 3 4 5 6

# n = 0
# while n <= 5:
#     n += 1
#     if n == 4:
#         break
#     print(n)                        # Output: 1 2 3

# n = 0
# while n <= 5:
#     n += 1
#     if n == 4:
#         pass
#     else:
#         print(n)                      # Output: 1 2 3 5 6

# myList = ['a', 'b', 'c', 'd']
# x = 0
# for i in myList:
#     print(myList[x])
#     x += 1                              # Output: a b c d

# for x in "Hello":
#     print(x)                            # Output: H e l l o

# for i in range(5):
#     print(i)                            # Output: 0 1 2 3 4

# for i in range(5, 10):
#     print(i)                            # Output: 5 6 7 8 9

# for x in range(5, 10, 3):
#   print(x)                              # Output: 5 8

# for i in range(5):
#     print(i)                            
# else:
#     print('Done')                       # Output: 0 1 2 3 4 Done


'''-------------------Functions-----------------------'''
'''Simple function with no return & no argument'''
# def myFun():
#     print('Hello from myFun')
# myFun()


'''Function with no return & 2 argument'''
# def myFun2(x, y):
#     print('sum = ', x+y)
# myFun2(5,1)



'''Function with return & 2 argument'''
# def myFun3(x, y):
#     return x+y
# print(myFun3(2,6))

'''-------------------Class & Method-----------------------'''
'''Simple Class'''
# class MyClass:
#     def dis(self):
#         print('Hello from MyClass')
# obj1 = MyClass()
# obj1.dis()                      # Output: Hello from MyClass
                        
'''Class with Constructor'''
# class MyClass2:
#     def __init__(self):
#          print('Hello from constructor')
#     def dis(self):
#         print('Hello from MyClass2')
# obj2 = MyClass2()
# obj2.dis()                      # Output: Hello from constructor
#                                 #         Hello from MyClass2

'''Circle's area calculation by using Class'''
# class Circle:
#     pi = 3.14
#     def __init__(self, r):
#          self.r = r
#     def area(self):
#         return Circle.pi * (self.r ** 2)
# obj3 = Circle(2)
# print(obj3.area())              # Output: 12.56

'''-------------------try, except, except, ..., except, else, finally-----------------------'''
'''Simple try, except'''
# try:
#     print(2/0)
# except:
#     print("Can't divide by zero")               # Output: Can't divide by zero


'''Try, except when exception type is known in-advance'''
# try:
#     print(2/0)
# except ZeroDivisionError:
#     print("Can't divide by zero")               # Output: Can't divide by zero


'''Try, except with built-in error messages'''
try:
    print(2/0)
except ZeroDivisionError as er1:
    print(er1)
except Exception as er2:
    print(er2)                                  # Output: division by zero


'''Try, except, else, finally'''
# try:
#     print(2/0)
# except Exception:
#     print('Error')
# else:
#     print('Successfully divided')
# finally:
#         print("I don't care if there is error or not")      # Output: Error
#                                                             #         I don't care if there is error or not



'''More than one exception types separately '''
# try:
#     x = int(input('Enter value for x '))
#     y = int(input('Enter value for y '))
#     print(x/y)
# except ValueError:
#     print('Please enter only numbers')
# except ZeroDivisionError:
#     print('Please enter y higher than 0')
# except ZeroDivisionError:
#     print('This will never be displayed')
# except:
#     print('Unknown error')


'''Merging more than one exception types'''
# try:
#     x = int(input('Enter value for x '))
#     y = int(input('Enter value for y '))
#     print(x/y)
# except (ValueError, ZeroDivisionError):
#     print('Please enter only number and higher than 0')
# except:
#     print('Unknown error')


'''raising errors programmatically'''
# try:
#     raise ZeroDivisionError
#     raise Exception
#     print('No')
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except:
#     print("Unknown Error")              # Output: Can't divide by zero

#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
#?
# '''''''''I have one question for you. Ready? What is O/P of the below code?
# '''''''''
# try:
#     print(2/'a')
# except:
#     print("Unknown Error")
# except ZeroDivisionError:
#     print("Can't divide by zero")





# '''''''''No, the answer is 'error', b/s the default 'except' must be at the last
# '''''''''


'''''''''''''''''''''''''''''End'''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


'''----------------------------Exercise--------------------------'''
'''1 - Write a python program that converts number to ordinal number.
        (Eg: 1 -> 1st, 2 -> 2nd, 3 -> 3rd, 4 -> 4th, 5 -> 5th, ... )

   2 - Write a python program that sort the a character in ascending order
        according to their respective probability value.
        (
        Eg: 
            How many numbers do you have? 
            3
            Enter character # 1 and its probability:
            a
            0.28
            Enter character # 2 and its probability:
            b
            0.23
            Enter character # 3 and its probability:
            c
            0.49

            Sorted result is : c a b
        )'''
