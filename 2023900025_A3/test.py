# 1. Find highest number in an array - [5,2,4,1,8,6,7]

ar = [5,2,4,1,8,6,7]
m = ar[0]
for i in range(1,7,1): #start,stop,step
    if(ar[i]>m):
        m = ar[i]
print(m)
        
# 2. Find minimum number in an array - [5,2,4,1,8,6,7]
# solved

# 3. Prime Number

num = int(input("Enter a number :"))

prime = True
for i in range(2,num//2 + 1,1):
    if num % i == 0 :
        prime = False
        break

if prime is True:
    print("Prime number")
else:
    print("Not a prime  number")

# 3. print all the multiples of a number input - 20 output - 2,4,5,10 