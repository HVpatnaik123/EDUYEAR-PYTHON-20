#assignment-1

my_list = [1,6,7,8,9,10,11,2,3,4,5]

even_list = []
odd_list = []
print(my_list)
for item in my_list:
    if item%2==0:
       even_list.append(item)
       
    else:
        odd_list.append(item)
        
print(even_list)
print("Number of even elements are: ", len(even_list))
print(odd_list)
print("Number of odd elements are: ", len(odd_list))


#assignment-2

my_list = [1,6,7,8,9,10,11,2,3,4,5]

my_list.sort()
print("Minimum Number is: ", my_list[0])

my_list.sort(reverse = True)
print("Maximum Number is: ", my_list[0])


#assignment-3 (showing me a syntax error. please rectify my mistake)

my_list = []

for item in range(0, 100):
    user_inp = int(input("enter your number to list: ")
    my_list.append(user_inp)
    if user_inp =='q':
        x = my_list[::-1]
        if x==my_list:
            print("list is palindrome")
            print(my_list)
        else:
            print("Not a palindrome")
            print(my_list)    
    

