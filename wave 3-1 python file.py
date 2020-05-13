def primeFactorization(value):
    if value < 2:
        print("The value must be 2 or greater.")
    else:
        print("The prime factors of " + str(value) + " are:")
        
        
        factor = 2
        while factor <= value:
           
            if value % factor == 0:
                print(factor)
                value = value // factor
            else:
                factor += 1

if __name__ == "__main__":
   

    value = int(input("Enter an integer (2 or greater): "))
    primeFactorization(value)
