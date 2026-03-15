import json
def add_student():
   name = input("Enter a name of the student :")
   stud_id = int(input("Enter a student id :"))
   stud_age = int(input("Enter a student age :"))
   stud_marks = int(input("Enter the student marks :"))
   d = {
      'name' : name,
      'student_id' : stud_id,
      'stud_age' : stud_age,
      'stud_marks' : stud_marks
    }
   with open('student.json','r') as f:
      data = json.load(f)
   data.append(d)
   with open('student.json','w') as f:
      json.dump(data,f,indent=4)
def update_student():
   st_id = int(input("Enter the student id :"))
   with open('student.json','r') as f:
      student = json.load(f)
   found = False
   for st in student:
      if st["student_id"] == st_id:
         found = True
         print("Student Found ", st)
         st['name'] = input("Enter a number :")
         st['stud_age'] = input("Enter a age:")
         st['stud_marks'] = input('Enter a marks :')
   if found == False: 
      print("Student Not Found") 
   with open('student.json','w') as f:
      json.dump(student,f,indent = 4)
def view_student():
   with open('student.json','r') as f:
      st = json.load(f)
   for s in st:
      print(s)
def file_clear():
   with open('student.json','w') as f:
      json.dump([],f)
while True:
   print("""
   1.Add Student
   2.Update Student
   3.View Student
   4.File Clear
   5.exit
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
   else:
      break
