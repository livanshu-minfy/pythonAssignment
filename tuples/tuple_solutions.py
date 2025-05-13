# ------------------------------------------------------ EASY QUESTIONS ------------------------------------------------------
'''
Tuple Basics
Write a function called `swap_pairs` that swaps adjacent elements in a tuple. If the tuple has an odd length, the last element should remain in place.'''

def swap_pairs(tup):
    result = []
    for i in range(0, len(tup) - 1, 2):
        result.append(tup[i+1])
        result.append(tup[i])
    if len(tup) % 2 == 1:
        result.append(tup[-1])
    return tuple(result)

# Example usage:
print(swap_pairs((1, 2, 3, 4)))  # Should return (2, 1, 4, 3)
print(swap_pairs((1, 2, 3)))  # Should return (2, 1, 3)

'''
Tuple Unpacking
Write a function called `get_stats` that takes a list of numbers and returns a tuple containing the minimum, maximum, sum, and average of the numbers.'''

def get_stats(nums):
    if not nums:
        return (None, None, 0, 0)
    total = sum(nums)
    average = total / len(nums)
    return (min(nums), max(nums), total, average)

# Example usage:
print(get_stats([1, 2, 3, 4, 5]))  # Should return (1, 5, 15, 3.0)


# ------------------------------------------------------ MEDIUM QUESTIONS ------------------------------------------------------

'''
Named Tuples
Create a named tuple called `Student` with fields for name, age, and grades (which should be a tuple of numbers). Then write a function called `top_student` that takes a list of Student tuples and returns the Student with the highest average grade.'''

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])

def average(student):
    return sum(student.grades) / len(student.grades)

def top_student(students):
    return max(students, key=average)

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))  # Should return the charlie Student tuple


'''
Tuple as Keys
Create a function called `count_coordinate_occurrences` that takes a list of (x, y) coordinate tuples and returns a dictionary mapping each coordinate to the number of times it appears in the list.'''

def count_coordinate_occurrences(coords):
    count = {}
    for coord in coords:
        if coord in count:
            count[coord] += 1
        else:
            count[coord] = 1
    return count

# Example usage:
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
# Should return {(1, 2): 3, (3, 4): 2, (5, 6): 1}

# ------------------------------------------------------ HARD QUESTIONS ------------------------------------------------------

'''
Complex Data Structure
Create a function called `group_by_department` that takes a list of employee tuples in the format (name, department, salary) and returns a dictionary where keys are departments and values are tuples with two elements: the average salary and a list of employee names in that department.'''

def group_by_department(employees):
    result = {}

    for name, dept, salary in employees:
        if dept not in result:
            result[dept] = {"total_salary": 0, "count": 0, "names": []}
        
        result[dept]["total_salary"] += salary
        result[dept]["count"] += 1
        result[dept]["names"].append(name)

    final = {}
    for dept, data in result.items():
        avg_salary = data["total_salary"] // data["count"]
        final[dept] = (avg_salary, data["names"])
    
    return final

# Example usage:
employees = [
    ("Alice", "Engineering", 80000),
    ("Bob", "Marketing", 70000),
    ("Charlie", "Engineering", 90000),
    ("Diana", "HR", 65000),
    ("Eve", "Marketing", 75000)
]

result = group_by_department(employees)
print(result)
# Should return:
# {
#   "Engineering": (85000, ["Alice", "Charlie"]),
#   "Marketing": (72500, ["Bob", "Eve"]),
#   "HR": (65000, ["Diana"])
# }


'''
Recursive Tuple Processing
Write a function called `flatten_tuple` that takes a nested tuple of arbitrary depth and returns a single flat tuple containing all the elements in the original order.'''

def flatten_tuple(tup):
    result = ()

    for item in tup:
        if isinstance(item, tuple):
            result += flatten_tuple(item)
        else:
            result += (item,)
    
    return result

# Example usage:
nested = (1, (2, 3), (4, (5, 6)), 7)
print(flatten_tuple(nested))  # Should return (1, 2, 3, 4, 5, 6, 7)