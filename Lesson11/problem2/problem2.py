print('-' * 60)
print('Narrative Bot: ')

name = input('Student Name: ')
grade = input('Grade: ')



print()

print(name + ', your final grade in AP Computer Science is ' + grade + '%.')

if grade >= '65':
	print('You have excelled in all components of the class! I wish you continued success in the next semester of AP Computer Science!')
else:
	print('This largely a result of missing projects and homeowrk assignments. Unfortunately, because this grade is less than a 65, you will have to complete an MBA assignment next semester.')

print('-' * 60)
