#black list students and white list students, number of students arego in to graduate
black_list = ['ravi' , 'raj' , 'raju' ]

number_student = int(input("total number of student in class: "))
student_list=[]
white_list=[]

for student in range(number_student):
  prompt = input("enter the name of students : ")
  if prompt == "":
    prompt = input(" please enter the name of students : ")
  student_list.append(prompt)

for student in student_list:
  if student not in black_list:
    white_list.append(student)

print ("This "+ str(len(white_list)) + " number of student are passed ")
print(*sorted(white_list), sep='\n')