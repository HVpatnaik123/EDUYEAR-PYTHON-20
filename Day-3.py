
#assignment -1

user_inp = int(input("enter your year of birth: "))
current_year = 2021

age = current_year - user_inp
print("you are", age, "years old")


#assignment -2

num1 = int(input("Enter 1st No.: "))
num2 = int(input("Enter 2nd No.: "))

print("sum is: ", num1+num2)
print("Difference is: ", num1-num2)
print("Multiplication is: ", num1*num2)
print("Division is: ", num1/num2)
print("Remainder is: ", num1%num2)
print("Round-off division is: ", num1//num2)
print("Power is: ", num1**num2)


#assignment -3
var1 = "python Programming"

print("number of occurance of p is: ", var1.lower().count('p'))


#assignment -4
user_inp = input("enter your input string: ")

print(user_inp[0::2])#1st way
print(user_inp[::2])#2nd way
print(user_inp[0:len(user_inp):2])#3rd way


