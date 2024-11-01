# Используем немецкий алфавит
german_alphabet = "abcdefghijklmnopqrstuvwxyzäöüß"
# Заменяет все символы в строке, не входящие в список allowed_chars, на пустую строку.
def custom_sub(allowed_chars, text):
    result = []
    for char in text:
        if char in allowed_chars.lower():
            result.append(char)
    return ''.join(result)

# текст для очистки от символов не входящие в алфавит
text = "Lorem Ipsum ist - ;einfach,,,, nur ein + - / @@Blindtext der Druck 258 4!!№;%%"

# # Проверяем работу функции
# filtered_text = custom_sub(german_alphabet, text)
# print("Отфильтрованный текст:", filtered_text)



def create_frequency_dict(text):
    # Приводим текст к нижнему регистру и оставляем только немецкие буквы
    text = custom_sub(german_alphabet, text)
    # print("Отфильтрованный текст:", text)

    # Инициализируем частотный словарь с нулевыми значениями для каждой буквы
    frequency_dict = {letter: 0 for letter in german_alphabet}

    # Подсчитываем частоту каждой буквы
    for letter in text:
        if letter in frequency_dict:
            frequency_dict[letter] += 1

    return frequency_dict

# Пример текста на немецком
text = """
    йцукеVolkswagen steht vor einer Zäsur: Der Konzern plant die Schließung von drei Werken in Deutschland und den 
    Abbau zahlreicher Arbeitsplätze. Gleichzeitig verabschiedet sich VW von seinem Grundsatz, bezahlbare Autos 
    für die breite Masse anzubieten – ein „Volkswagen fürs Volk“ scheint Geschichte. Die Entscheidung trifft 
    auf hohe Produktionskosten und Preisdruck, doch was bedeutet das für Mitarbeiter, die deutsche Industrie 
    und Millionen potenzieller Kunden?
    Nun könnte man argumentieren, die Corona-Pandemie, die Halbleiterkrise, der Krieg in der Ukraine und hohe 
    Energiekosten ließen die Autopreise in die Höhe schießen und senkten die Kauflust. Doch die Probleme liegen 
    gerade bei VW woanders. Es sind tatsächlich die hohen Preise und die Tatsache, dass VW keine erschwinglichen 
    Kleinwagen im Programm hat. Selbstverständlich könnte der VW e-up ins Feld geführt werden, aber der startet 
    erst bei 30.000 € bei einer Reichweite von rund 250 km. Zum Vergleich: Der größere Dacia Spring 45 mit einer 
    ähnlichen Reichweite ist bereits ab 20.000 € erhältlich.
"""

text = 'sfdfs'
# Создаем частотный словарь для немецкого текста
frequency_dict = create_frequency_dict(text)

# Выводим частотный словарь
for letter, freq in frequency_dict.items():
    print(f"{letter}: {freq}")