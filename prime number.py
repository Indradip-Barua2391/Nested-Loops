lower = int(input("Enter the Lower Limit: "))
upper = int(input("Enter the Upper Limit: "))

for num in range(lower, upper+1):
    
    if num > 1:
        
        for i in range (2,num):
            
            if num % i == 0:
                print(f"The number {num} is not a prime number")
                break
            else:
                print(f"The number {num} is not a prime number")