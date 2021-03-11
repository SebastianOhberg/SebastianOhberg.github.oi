#This is a example to create a loop to fill out a list in python

example_lists = []

for example_list in range(10):          #This loop is used to fill out wthi numbers from 0 to 9
	example_lists.append(example_list)

print(example_lists)

students = []

for student in range(3):						#This loop is used to fill a 3 students names on a list
	student = input('Please white the student name: ') #When use input(print('text') ) python prints none first
	students.append(student)						#The .append method is used to create a "NEW ITEM" in the lists

print(students)
