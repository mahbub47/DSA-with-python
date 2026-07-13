# Day 02: 30 days of python programming

first_name = "Mahbub"
last_name = "Ashik"
full_name = "Mahbub Ahmed Ashik"
country = "Bangladesh"
city = "Sylhet"
age = 25
year = 2026
is_married = False
is_true = True
is_light = False
name, cgpa, is_graduated = "Mahbub Ahmed Ashik", 3.44, True

print("Type of first_name is ", type(first_name))
print("Type of last_name is ", type(last_name))
print("Type of full_name is ", type(full_name))
print("Type of country is ", type(country))
print("Type of city is ", type(city))
print("Type of age is ", type(age))
print("Type of year is ", type(year))
print("Type of is_married is ", type(is_married))
print("Type of is_true is ", type(is_true))
print("Type of is_light is ", type(is_light))
print("Type of name, cgpa, and is_graduated is ", type(name), type(cgpa), type(is_graduated))


print("Length of my first_name is ", len(first_name))

print(f"Length of my first_name {'>=' if len(first_name) >= len(last_name) else '<='} length of my last_name")

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(division)

radius = 30.0
area_of_circle = 3.1416 * (radius ** 2)
circum_of_circle = 2 * 3.1416 * radius

r = float(input("Enter the radius of the circle: "))
area = 3.1416 *  (r ** 2)

first_name, last_name, country, age = input("Enter first name: "), input("Enter last name: "), input("Enter country name: "), int(input("Enter age: "))

