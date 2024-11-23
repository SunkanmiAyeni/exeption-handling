try:
    num1=int(input("Please enter a number"))
    num2=int(input("Please enter a number"))
    result=num1/num2
    print("result",result)
except ZeroDivisionError:
    print("number is not divisable with zero")
except ValueError:
    print("Please enter a valid number")
except:
    print("an error occoured")
finally:
    print("this is always going to RUN")