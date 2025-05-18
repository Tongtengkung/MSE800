# # In-class activity 1
# # 1. Create a list of numbers from 1 to 10 and print the list.
# numbers = [1, 2, 3, 4, 5]
# squares = {str(n): n**2 for n in numbers}
# print(squares)

# # 2. Create a dictionary comprehension that generates a dictionary with numbers as keys and their squares as values.
# even_squares = {str(n): n**2 for n in numbers if n % 2 == 0}
# print(even_squares)

# # 3. Create a dictionary with keys as letters and values as their ASCII values.
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# dictionary = {k: v for k, v in zip(keys, values)}
# print(dictionary)

# # 4. Merge two dictionaries into one.
# dict1 = {'a': 1, 'b': 2}                                    
# dict2 = {'b': 3, 'c': 4}
# merged_dict = {**dict1, **dict2}                                                    
# print(merged_dict)

# # 5. Create a dictionary with numbers as keys and their cubes as values.
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5, 'e': 6}
# merged_dict = {**dict1, **dict2, **dict3}

# 6. Merge two dictionaries with a condition that only keys present in both dictionaries are included.
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 3, 'e': 4, 'f': 5}
# merged_dict = {**{k:v for k, v in dict1.items() if v in 'aeiou'}, 
#                **{k:v for k, v in dict2.items() if v in 'aeiou'}}
# print(merged_dict)    

# file_name, _ = "filename.txt".split('.')
# print(_)  # Output: filename

# for _ in range(5):
#     print("Hello, I don't care about the numbers.")

# x, _ , y = (1,[1,2,3],3)
# print(x, _, y)  # Output: 1 3

# name = ['Mo', 'Alex', 'Ethan', 'Yan', ' Shela', 'Miky']
# for i, name in enumerate(name,start=1):
#     print(i, name)  # Output: 0 a, 1 b, 2 c

# name = ['Alice', 'Bob', 'Cathy']
# ages = [25, 30, 22]
# paired = zip(name, ages)
# print(list(paired))

# ids = [1, 2, 3]
# names = ['Alice', 'Bob', 'Cathy', 'Mike']
# grades = ['A', 'B', 'A+', 'A']
# student_dict = {id_: f"{name}: {grade}" for id_, name, grade in zip(ids, names, grades)}
# print("Dictionary:", student_dict)

# data = []
# for i in range(5):
#     data.append(lambda a, i=i*2: i*a)

# data = []
# def mul(m):
#     def multiply(a):
#         return m * a
#     return multiply

# for i in range(5):
#     data.append(mul(i * 2))
    
# print(data[4](5))  # [i](a)



