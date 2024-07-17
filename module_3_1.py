calls = 0 #Создали переменную calls = 0 вне функций
def count_calls(): # Создать функцию count_calls
    global calls # т. к. функция должна вызываться в остальных двух функциях
    calls += 1 # изменяем в ней значение переменной calls
    return calls # возвращаяем переменную calls, нужно ли это и для чего :(?
def string_info(string): # Создать функцию string_info с параметром string
    count_calls() # это не совсем понятно для чего мы делаем?
    return (len(string), string.upper(), string.lower()) #возвращает кортеж из: длины этой строки, строку
    # в верхнем регистре, строку в нижнем регистре.
def is_contains(string, list_to_search): #Создать функцию is_contains с двумя параметрами string
    # и list_to_search
    count_calls() # ???
    return string.upper() in [s.upper() for s in list_to_search] # возвращает True, если строка находится
    # в этом списке, False - если отсутствует
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)