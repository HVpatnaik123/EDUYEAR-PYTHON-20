
#assignment-1
def prime_check(num):
    for i in range (2,num):
        if num % i == 0:
            print('number {} is not a prime'.format(num))
            break
        else:
            print('{} is a prime number'.format(num))
            break
inp = int(input(' Enter number: '))
prime_check(inp)

#assignment-2

def fact(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    print('Factorial of {} is:'.format(num), factorial)

inp = int(input('enter a number: '))
fact(inp)
    
