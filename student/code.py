# --------------
# Code starts here
class_1 = ['Geoffrey Hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
# Create the lists 
class_2 = ['Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
# Concatenate both the strings
new_class= class_1+class_2
print(new_class)
new_class.append('Peter Warden')
# Append the list
print(new_class)
# Print updated list
new_class.remove('Carla Gentry')
print(new_class)
# Remove the element from the list

# Print the list

courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
# Create the Dictionary
print(courses)
total= sum(courses.values())
print(total)
percentage= total/5
# Slice the dict and stores  the all subjects marks in variable
print(percentage)

# Store the all the subject in one variable `Total`
mathematics= {'Geoffrey Hinton':78, 'Andrew Ng':95, 'Sebastian Raschka':65, 'Yoshua Bengio':50,'Hilary Mason':70, 'Carla Gentry':66, 'Corinna Cortes':75}
topper=max(mathematics,key = mathematics.get)
print(topper)
first_name=topper.split()[0]
last_name=topper.split()[1]
full_name= last_name + " " + first_name
certificate_name= full_name.upper()
print(certificate_name)



