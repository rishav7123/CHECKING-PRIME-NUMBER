num = int(input("Enter the number: "))
if num == 1:
    print("It is not a prime number.")

for i in range(1, num):    

    if num % 2 == 0:
        print("It is not a prime number.")
        break

    else:
        print("It is a prime number.")        
        break
