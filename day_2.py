##Exercises: Level 1##

#Day 2: 30 days of pythonprogramming#

first_name = 'Lukas' 
last_name = 'Hirst'
full_name = 'Lukas Hirst'
home_country = 'Canada'
home_city = 'Vancouver'
age = 15
current_year = 2026
is_married = False
is_true = False
is_light_on = True
first_home, current_home, first_city = '1291', '1250', 'Vancouver'

##Exercises: Level 2##

#Print the type of each variable#

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(home_country))
print(type(home_city))
print(type(age))
print(type(current_year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(first_name), type(first_city), type(current_year))

print(len(first_name))

first_name_length = len(first_name)
last_name_length = len(last_name)

differnce = first_name_length - last_name_length

print(differnce)

#Add num_one and num_two and assign the value to a variable total

num_one = 5
num_two = 4

total = num_one + num_two

diff = num_two - num_one

product = num_one * num_two

division = num_one / num_two

remainder = num_two % num_one

exp = num_one ** num_two

floor_division = num_one // num_two

area_of_circle = 3.14159 * 30 ** 2

circum_of_circle = 2 * 3.14159 * 30

circle_radius = float(input("Radius: "))

print(3.14159 * circle_radius ** 2)

real_first_name = input('Whats your name?')

real_last_name = input('Whats your last name?')

real_country = input('In which country do you live?')

real_age = input('Whats your age?')

print(real_first_name)
print(real_last_name)
print(real_country)
print(real_age)