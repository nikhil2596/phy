def prime():
    num = int(input("Enter a nnumber : "))
    count = 0
    if(num > 1):
        if(num == 2):
            print("%d is a prime number"%num)
        else:
            for i in range(2,num):
                if((num%i) == 0):
                    count += 1
                    break
            if(count == 0):
                print("%d is a prime number."%num)
            else:
                print("%d is not a prime number."%num)
    else:
        print("%d is not a prime number"%num)
prime()
