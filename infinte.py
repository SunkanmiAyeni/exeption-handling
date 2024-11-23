valid=False
while not valid:
    try:
        p=int(input("Please enter a number"))
        if p%2==0:
            print("Its an even number Byebye")
            valid=True
    except:
        print("Some error occured")