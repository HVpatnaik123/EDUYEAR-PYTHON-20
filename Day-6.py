
#assignment-1
'''
a = 'AbcdefghIjk'
b = list(a.lower())
print(b)
count = 0
for i in b:
    if i =='a' or i == 'e' or i =='i' or i=='o' or i=='u':
        print(b.index(i), i)
'''

a = 'HArsha PatnAIk'
b = list(a.lower())

print(b)
count_a, count_i = 0 , 0
for i in b:
    
    if i =='a':
        count_a +=1
print('count of a: {}'.format(count_a))

for i in b:
    if i =='i':
        count_i +=1
print('count of i: {}'.format(count_i))

#assignment-2
        
a = 'hello world happy birthday'

b = a.split( )
print(b)
b.reverse()
print(b)


#assignment-3
a = [1,2,3,3,2,4]
a.sort()
print(a)
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
