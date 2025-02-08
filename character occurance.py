
string = input("Please enter your own word : ")

char = input("Please enter a Character that you want to check : ")
i = 0
count = 0

while(i < len(string)):
    
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The total Number of Times ", char, " has Occurred = " , count)