# Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
# количество пробельных символов. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно заменив символы третей строки их числовыми
# кодами.


def do_it():
    with open('All_PZ/PZ_10/text18-14.txt', 'r+', encoding="utf-8") as file1:       # Открытие первого файла
        text = str(file1.read())                                                    # Чтение значений
        print(str(text) + '\n')                                                     # Вывод
        print(str(str(text).count(' ')) + ' пробелов' + '\n')                       # Вывод
        k = 0
        z = ''
        for i in text.split('\n'):                                                  # Поиск 3 строки
            k += 1
            if k == 3:
                z = i
        k = []
        for i in z:                                                                 # Замена букв на их код
            k.append(ord(i))
        text = text.replace(z, str(k))                                              # Замена строки

    with open('All_PZ/PZ_10/second.txt', 'w+', encoding='utf-8') as file2:          # Открытие первого файла
        file2.write(str(text))                                                      # Запись результата
        print(text)                                                                 # Вывод

    file1.close()                                                                   # Закрытие
    file2.close()                                                                   # Закрытие
