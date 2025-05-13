# ------------------------------------------------------ EASY QUESTIONS ------------------------------------------------------

'''
Dictionary Basics
Write a function called `invert_dictionary` that takes a dictionary and returns a new dictionary where the keys become values and values become keys'''

def invert_dictionary(dict):
    result = {}
    for key, value in dict.items():
        result[value] = key
    return result

print(invert_dictionary({"a": 1, "b": 2, "c": 3}))
# Output: {1: 'a', 2: 'b', 3: 'c'}

'''
Dictionary Operations
Write a function called `merge_dictionaries` that takes two dictionaries and merges them. If a key exists in both dictionaries, the value from the second dictionary should be used.'''

def merge_dictionaries(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result


# Example usage:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Should return {"a": 1, "b": 3, "c": 4}


# ------------------------------------------------------ MEDIUM QUESTIONS ------------------------------------------------------

'''
Dictionary Comprehensions
Write a function called `word_frequencies` that takes a string of text and returns a dictionary mapping each word to its frequency (count of occurrences).'''

def word_frequencies(text):
    words = text.split()
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

# Example usage:
text = "the quick brown fox jumps over the lazy dog"
print(word_frequencies(text))
# Should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}


'''
Nested Dictionaries
Create a function called `add_contact` that manages a nested dictionary representing a contact book. The function should add a new contact with details or update an existing contact.'''

def add_contact(contacts, name, **info):
    if name not in contacts:
        contacts[name] = {}
    contacts[name].update(info)

# Example usage:
contacts = {}
add_contact(contacts, "Alice", phone="123-456-7890", email="alice@example.com")
add_contact(contacts, "Bob", phone="987-654-3210")
add_contact(contacts, "Alice", address="123 Main St")  # Updates Alice's info

print(contacts)
# Should return:
# {
#   "Alice": {"phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
#   "Bob": {"phone": "987-654-3210"}
# }


# ------------------------------------------------------ HARD QUESTIONS ------------------------------------------------------

'''
Dictionary Transformations
Create a function called `transform_grades` that takes a dictionary where keys are student names and values are lists of grades. Return a new dictionary where keys are still student names, but values are dictionaries containing: 'average' (the average grade), 'highest' (the highest grade), and 'lowest' (the lowest grade).'''

def transform_grades(grades):
    result = {}
    for student, scores in grades.items():
        result[student] = {
            "average": sum(scores) / len(scores),
            "highest": max(scores),
            "lowest": min(scores)
        }
    return result

# Example usage:
grades = {
    "Alice": [85, 90, 95],
    "Bob": [70, 80, 90],
    "Charlie": [90, 92, 93]
}

print(transform_grades(grades))
# Should return:
# {
#   "Alice": {"average": 90.0, "highest": 95, "lowest": 85},
#   "Bob": {"average": 80.0, "highest": 90, "lowest": 70},
#   "Charlie": {"average": 91.67, "highest": 93, "lowest": 90}
# }


'''
Advanced Dictionary Operations
Implement a function called `generate_tree` that takes a list of file paths (like ["folder1/file1.txt", "folder1/folder2/file2.txt", "folder3/file3.txt"]) and generates a nested dictionary representing the file structure.'''

def generate_tree(paths):
    tree = {}
    for path in paths:
        parts = path.split("/")
        current = tree
        for part in parts:
            current = current.setdefault(part, {})
    return tree

# Example usage:
paths = [
    "folder1/file1.txt",
    "folder1/folder2/file2.txt",
    "folder3/file3.txt"
]

print(generate_tree(paths))
# Should return:
# {
#   "folder1": {
#     "file1.txt": {},
#     "folder2": {
#       "file2.txt": {}
#     }
#   },
#   "folder3": {
#     "file3.txt": {}
#   }
# }
