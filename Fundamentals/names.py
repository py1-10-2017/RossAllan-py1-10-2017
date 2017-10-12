#Part 1
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def name_extract(namelist):
    for element in namelist:
        print element['first_name'],element['last_name']
name_extract(students)
#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def user_extract(userlist):
    for key in userlist:
        print key
        usercount=1
        for element in userlist[key]:
            print str(usercount)+" - "+element['first_name']+" "+element['last_name']+" - "+str((len(element['first_name'])+len(element['last_name'])))
            usercount+=1
user_extract(users)
