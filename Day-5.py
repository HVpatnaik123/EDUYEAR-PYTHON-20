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

#option-1
my_list.sort(reverse = True)
print("Maximum Number is: ", my_list[0])

#option-2
print("Maximum Number is: ", my_list[-1])   

#assignment-3 
'''
x = [1,2,3,2,4]

for item in x:
    z = x[::-1]
    if x[item] == z[item]:
            print("list is palindrome")
            print(x)
    else:
            print("Not a palindrome")
            print(x)        
    
'''
x = [1,2,3,2,1]
y = x[::-1]
if x==y:
    print('palindrome',x)
else:
    print('not a palindrome',x)
    

