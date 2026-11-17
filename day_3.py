#Declare your age as integer variable
age = 15
#Declare your height as a float variable
height = 71.5
#Declare a variable that store a complex number
complex_num = 12j+3
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
tri_height = float(input('HEIGHT:'))
tri_base = float(input('BASE:'))
print (' The area of the triangle is',.5 * tri_height * tri_base)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Whats side A?'))
side_b = int(input('Whats side B?'))
side_c = int(input('Whats side C?'))
peramiter_of_tri = (side_a + side_b + side_c)
print('The perimeter of the triangle is', peramiter_of_tri)
#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rec_length = int(input('Whats the width?'))
rec_width = int(input('Whats the length?'))
area_rectangle = (rec_length * rec_width)
peramiter_of_rec = (2 * (rec_length + rec_width))
print('The area of the rectangle is', area_rectangle)
print('The peramiter of the rectangle is', peramiter_of_rec)
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input('Whats the radius? '))
circle_area = (3.14 * radius ** 2)
circufrance = (2 * 3.14 * radius)
print('The circles area is', circle_area)
print('The circles circumfrance is', circufrance)
#Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope_1 = 2
y_intercept = -2
x_intercept = -y_intercept / slope_1
print(slope_1)
print(y_intercept)
print(x_intercept)
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("Slope:", slope_2)
print("Euclidean Distance:", distance)
#Compare the slopes in tasks 8 and 9.
print('Slopes from questions 8 and 9 are both the same =', slope_1 == slope_2)
