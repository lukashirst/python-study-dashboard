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