import re


# Проверка правильности HTML-тегов: Напишите функцию, которая проверяет, правильно ли вложены HTML-теги в строке.
# Например, строка <div><p></p></div> должна возвращать True, а <div><p></div></p> — False.



def is_valid_html(html_string):
    stack = []
    # Регулярное выражение для поиска HTML-тегов
    tags = re.findall(r'/?[a-zA-Z0-9]+', html_string)
    # print(tags)

    for tag in tags:
        if not tag.startswith('/'):  # Это открывающий тег
            stack.append(tag)
        else:  # Это закрывающий тег
            if not stack:  # Если стек пуст, это означает, что у нас нет соответствующего открывающего тега
                return False
            opening_tag = stack.pop()  # Удаляем последний открывающий тег из стека
            if opening_tag != tag[1:]:  # Сравниваем с закрывающим тегом
                return False

    return len(stack) == 0  # Если стек пуст, все теги были правильно закрыты

# Примеры использования
print(is_valid_html("<div><p></p></div>"))
print(is_valid_html("<div><p></div></p>"))
print(is_valid_html("<ul><li></li></ul>"))
print(is_valid_html("<a><b><c></b></c></a>"))
print(is_valid_html("<div><p><div></p></div>"))

