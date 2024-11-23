try:
    a=int(input("Please enter a number: "))
    print("we recieve the number",a)
except ValueError as ex:
    print("expetion arrised",ex)
finally:
    print("this is always going to run.")