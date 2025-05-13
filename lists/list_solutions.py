# ------------------------------------------------------ EASY QUESTIONS ------------------------------------------------------

'''
List Operations
Write a function called `filter_even_numbers` that takes a list of integers and returns a new list containing only the even numbers.'''

def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Example usage:
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))  # Should return [2, 4, 6]
print(filter_even_numbers([1, 3, 5]))  # Should return []

'''
List Manipulation
Write a function called `merge_sorted_lists` that takes two sorted lists and returns a new sorted list containing all elements from both lists.'''

def merge_sorted_lists(list1, list2):
    mergedList = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            mergedList.append(list1[i])
            i += 1
        else:
            mergedList.append(list2[j])
            j += 1
    mergedList.extend(list1[i:])
    mergedList.extend(list2[j:])
    
    return mergedList

# Example usage:
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Should return [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))  # Should return [1, 2, 3, 4, 5, 6]

# ------------------------------------------------------ MEDIUM QUESTIONS ------------------------------------------------------

'''
List Comprehensions
Write a function called `generate_matrix` that takes dimensions n and m, and returns an n×m matrix where each element at position (i,j) is calculated as i*j.'''

def generate_matrix(n, m):
    matrix = []
    for i in range (n):
        row = []
        for j in range (m):
            row.append(i * j)
        matrix.append(row)
    return matrix

# Example usage:
print(generate_matrix(3, 3))
# Output:
# [
#   [0, 0, 0],
#   [0, 1, 2],
#   [0, 2, 4]
# ]

'''
Nested Lists
Write a function called `transpose_matrix` that takes a matrix (list of lists) and returns its transpose (rows become columns and vice versa).'''

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposedMatrix = []

    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        transposedMatrix.append(row)

    return transposedMatrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))
# Should return:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]



# ------------------------------------------------------ HARD QUESTIONS ------------------------------------------------------

'''
Advanced List Operations
Write a function called `find_peaks` that takes a list of numbers and returns the indices of all "peaks" (elements that are greater than both of their neighbors).'''

def find_peaks(nums):
    peaks = []
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            peaks.append(i)
    return peaks

# Example usage:
print(find_peaks([1, 3, 2, 3, 5, 4, 3, 2, 3, 1]))  # Should return [1, 4, 8]


'''
List Algorithms
Implement a function called `rotate_list` that rotates a list to the right by k steps, without using built-in functions like slice assignment.'''

def rotate_list(nums, k):
    n = len(nums)
    k = k % n
    rotatedList = []

    for i in range(n - k, n):
        rotatedList.append(nums[i])

    for i in range(n - k):
        rotatedList.append(nums[i])

    return rotatedList

# Example usage:
print(rotate_list([1, 2, 3, 4, 5], 2))  # Should return [4, 5, 1, 2, 3]
print(rotate_list([1, 2, 3], 4))  # Should return [3, 1, 2]
