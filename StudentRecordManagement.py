import json
# CHECK EMAIL VALIDATION CODE
def validate_email(email):
   required_domain = ['.com','.org','.edu','.net','.in']
   if ' ' in email:
      return False
   if email.count('@') !=1:
      return False
   username , domain = email.split('@')
   if len(username) == 0:
      return  False
   if '.' not in domain:
      return False
   if not any(domain.endswith(i) for i in required_domain):
      return False
   if not username[0].isalnum() or not username[-1].isalnum():
      return False
   return True
# ADD STUDENT
def add_student():
   name = input("Enter a name of the student :")
   stud_id = int(input("Enter a student id :"))
   stud_age = int(input("Enter a student age :"))
   stud_marks = int(input("Enter the student marks :"))
   email = input("Enter the email :")
   if not validate_email(email):
      print("Invalid email")
      return
   with open('student.json','r') as f:
      data = json.load(f)
   for st in data:
      if st['student_id'] == stud_id:
         print('ID already Exists')
         return
   d = {
      'name' : name,
      'student_id' : stud_id,
      'stud_age' : stud_age,
      'stud_marks' : stud_marks,
      'email_id' : email
    }
   # with open('student.json','r') as f:
   #    data = json.load(f)
   data.append(d)
   with open('student.json','w') as f:
      json.dump(data,f,indent=4)
   print("Student Added Successfully")

# UPDATE STUDENT
def update_student():
   st_id = int(input("Enter the student id :"))
   with open('student.json','r') as f:
      student = json.load(f)
   found = False
   for st in student:
      if st["student_id"] == st_id:
         found = True
         print("Student Found ", st)
         st['name'] = input("Enter a name :")
         st['stud_age'] = int(input("Enter a age:"))
         st['stud_marks'] = int(input('Enter a marks :'))
         st['email_id'] = input("Enter email id :")
   if found == False: 
      print("Student Not Found") 
   with open('student.json','w') as f:
      json.dump(student,f,indent = 4)

# VIEW STUDENT
def view_student():
   with open('student.json','r') as f:
      st = json.load(f)
   for s in st:
      print(s)

# CLEARING DATABASE
def file_clear():
   with open('student.json','w') as f:
      json.dump([],f)

# DELETING STUDENT
def delete_student():
   with open('student.json','r') as f:
      student = json.load(f)
   id = int(input("Enter the id :"))
   new_list = []
   found = False
   for st in student:
      if st['student_id'] != id:
         new_list.append(st)
      else:
         found = True
   if(found):
      print("Student deleted successfully")
   else:
      print("Student not Found")
   with open('student.json','w') as f:
      json.dump(new_list,f,indent =4)

# SEARCHING STUDENT
def search_student():
   id = int(input("Enter a student id :"))
   with open('student.json','r') as f: 
      student = json.load(f)
   Found = False
   for st in student:
      if st['student_id'] == id:
         print('Student Found :',st)
         Found = True
         break
   if not Found:
      print("Student Not Found")
while True:
   print("""
   1.Add Student
   2.Update Student
   3.View Student
   4.File Clear
   5.Delete Student
   6.Search Student
   7.exit
   """)
   choice = input("Enter your Choice :")
   if choice == '1':
      add_student()
   elif choice == '2':
      update_student()
   elif choice == '3':
      view_student()
   elif choice == '4':
      file_clear()
   elif choice == '5':
      delete_student()
   elif choice == '6':
      search_student()
   else:
      break
