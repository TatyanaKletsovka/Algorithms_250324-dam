#Постройте частотный словарь букв немецкого или английского алфавита.
#Частотный словарь букв - это структура данных или набор информации,
#который содержит информацию о том, какие буквы встречаются в тексте и с какой частотой.

from collections import Counter
import string

text = "Текст: Build a frequency dictionary of letters of the German äöüß or English alphabet."

# filtered_text = ''.join(filter(str.isalpha, text.lower()))  # lambda c: c.isalpha() or c in 'äöüß'
filtered_text = ''.join(filter(lambda c: 'a' <= c <= 'z' or c in 'äöüß', text.lower()))
print(filtered_text)

dict_ = Counter(filtered_text)

print(dict(dict_))
# for letter, freq in sorted(dict.items()):
#     print(f"{letter}: {freq}")

