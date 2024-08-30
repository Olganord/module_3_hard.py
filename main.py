def calculate_structure_sum(data_structure):
    summa = 0
    flag_dict = 0
    if isinstance(data_structure, dict): # Определяет тип данных
        for key, value in data_structure.items(): # Возвращает итерируемый объект, состоящий из кортежей
            #                             (ключ, значение) словаря:  вместо {'a': 4, 'b': 5} будет  (a, 4, b, 5) и т.п.
            summa += calculate_structure_sum(key) # Суммирует количество ключей
            summa += calculate_structure_sum(value) # Суммирует значения
            flag_dict += 1
            print('Словарь ,', flag_dict)

    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa


data_structure = {'ab3': 0, 'b': 0}


result = calculate_structure_sum(data_structure)
print(result)
