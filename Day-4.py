#assignment-1

m = int(input('enter starting range: '))
n = int(input('enter end range: '))

for i in range(m,n+1):
    if i%5==0:
        print("No. divisible by 5: ", i)

    elif i%7==0:
        print("No. divisible by 7: ", i)



#assignment-3


sum = 0
while True:
    inp = input("enter input (interger or q to exit): ")
    if inp =='q':
        print("sum is: ", sum)
        break
    else:
        sum = sum+int(inp)
        print("Sum is: ", sum)


#assignment-4
num = int(input("enter a number: "))
factorial = 1

for i in range(1,num + 1,1):
       factorial = factorial*i
print("The factorial of",num,"is: ",factorial)
