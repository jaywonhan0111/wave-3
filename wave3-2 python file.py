def isPrime(n):
  if n <= 1:
    return False
for i in range(2, n):
  if n % i == 0:
    return False 
return True 

def main():
  value = int(input("Enter an integer: "))
  if isPrime(value):
    print(value,"is prime.")
  else:
    print(value,"is not prime.")

if __name__ == "__main__":
  main()