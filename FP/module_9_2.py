first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elem) for elem in first_strings if len(elem) > 4]
second_result = [(elem1, elem2) for elem1 in first_strings for elem2 in second_strings if len(elem1) == len(elem2)]
third_result = {elem: len(elem) for elem in first_strings + second_strings if len(elem) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
