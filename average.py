def get_average():
    with open("./Work/Python/test/tempatures.txt", "r") as file:
        data = file.readlines() #[1:] aynı anda slicing de yapılabilir.
    values = data[1:]
    values = [float(i) for i in values]
    average_local = sum(values) / len(values)
    return average_local

average = get_average()
print(average)

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     grades = [ float(i) for i in grades]
#     maximum_local = max(grades)
#     return maximum_local

# maximum_number = get_max()
# print(maximum_number)

# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     maximum = max(grades)
#     return maximum
    
# print(get_max())

# Function to Process a List 2
# The get_max function you created in the previous exercise returned 9.7. 
# In this exercise, you should:
# (1) change the function so this time it returns the following string:
# "Max: 9.7, Min: 9.2"
# where 9.7 is the maximum, and 9.2 is the minimum.
# Note: For the exercise to be marked as correct by the system, you should return the exact string "Max: 9.7, Min: 9.2"

def get_max_min():
    grades = [9.6, 9.2, 9.7]
    max_grade = max(grades)
    min_grade = min(grades)
    return f"Max: {max_grade}, Min: {min_grade}"
    
result = get_max_min()
print(result)

