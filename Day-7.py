courses = ['python', 'java', 'c#', 'machine learning', 'mongo db', 'flask', 'django']
name = input('Enter your name: ')
mail = input('enter your mail id: ')
user = {
'user_id' : 101,
'name' : name,
'email': mail,
'courses' : []
    }

while True:
    #for menu
    print('1. All Courses \n2. My Courses \n3. Edit profile \n0. Exit')
    user_inp = input('enter your choice: ')
    if user_inp == '0':
        print('thanks for your time')
        break
    if user_inp =='1':
        #show all courses
        for i in courses:
            print(courses.index(i)+1, i)
        inp_course = int(input('enter your course number: '))
        course_add = courses[inp_course-1] 
        user['courses'].append(course_add)
        print(user)
    if user_inp =='2':
        print('you have enrolled for the below courses:')
        for i in user['courses']:
            
            print(user['courses'].index(i)+1, i)
    if user_inp == '3':
        new_name = input('enter new name: ')
        user['name'] = new_name
        print('hello', user['name'])
        new_mail = input('enter new mail id: ')
        user['email'] = new_mail
        print(user.values())
        
        
    
