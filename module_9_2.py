first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(item) for item in first_strings if len(item) >= 5]
second_result = [(first_item, second_item)
                 for first_item in first_strings
                 for second_item in second_strings
                 if len(first_item) == len(second_item)]
third_result = {item: len(item) for item in first_strings + second_strings if not len(item) % 2}

print(first_result) # список длин строк списка first_strings, если длина строки first_strings не менее 5 символов
print(second_result) # список из пар слов(кортежей) одинаковой длины строк first_strings и second_strings
print(third_result) # словарь с ключом-значением строка-длина строки списков first_strings и second_strings