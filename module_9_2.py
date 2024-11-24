first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(str_1) for str_1 in first_strings if len(str_1) > 5]
second_result = [(str_1, str_2) for str_1 in first_strings for str_2 in second_strings if len(str_1) == len(str_2)]

third_strings = first_strings + second_strings
third_result = {str_3: len(str_3) for str_3 in third_strings if len(str_3) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
