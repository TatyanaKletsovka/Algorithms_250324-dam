def is_palindrome(s):
    stack = []
    # Убираем пробелы и приводим строку к нижнему регистру для сравнения
    cleaned_string = ''.join(s.split()).lower()

    # Добавляем символы строки в стек
    for char in cleaned_string:
        stack.append(char)

    # Проверяем, является ли строка палиндромом
    for char in cleaned_string:
        if char != stack.pop():  # Сравниваем с последним добавленным символом из стека
            return False

    return True

# Примеры использования
print(is_palindrome("madam"))           # True
print(is_palindrome("hello world"))     # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("No lemon no melon")) # True
print(is_palindrome("Python"))          # False
