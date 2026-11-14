# 1. Basic Math & Operators (from 30-Days-Of-Python Day 1)
print("Addition:", 3 + 4)
print("Subtraction:", 3 - 4)
print("Multiplication:", 3 * 4)
print("Division:", 3 / 4)
print("Exponential:", 3 ** 4)
print("Modulus (Remainder):", 3 % 4)
print("Floor Division:", 3 // 4)

# 2. Checking Data Types (the building blocks of your dashboard)
print(type(10))                  # int (e.g., study streak days)
print(type(0.75))                # float (e.g., 0.75 hours = 45 mins)
print(type("Lukas"))             # str (e.g., your username)
print(type(True))                # bool (e.g., daily habit completed)
print(type(["Variables", "Lists"])) # list (e.g., topics learned)
print(type({"day": 1, "mins": 40})) # dict (e.g., a daily log entry)

# 3. Mini Dashboard Warmup: Calculate Euclidean Distance
# (Classic Day 1 exercise from the repo: distance between (2, 3) and (10, 8))
distance = ((10 - 2) ** 2 + (8 - 3) ** 2) ** 0.5
print("Euclidean Distance:", (distance))
