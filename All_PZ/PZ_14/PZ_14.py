import re


def res():
    print("""В исходном текстовом файле (hotline1.txt) найти все номера телефонов,
            соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
            элементов. После фразы «Горячая линия» добавить фразу «Министерства
            образования Ростовской области», выполнив манипуляции в новом файле.""")
    with open('All_PZ/PZ_14/hotline1.txt', 'r', encoding="utf-8") as file:      # file opening
        text = str(file.read())                                                 # Reading text
        print(text)

        def part1():                                                            # First part of task
            pattern = r"\d\(\d{3}\)\d{3}\-\d{2}\-\d{2}"                         # Making pattern
            count = re.findall(pattern, text)                                   # find all same phone numbers
            print(f"Похожие на задание номера: {count}, "
                  f"их количество: {len(count)}")

        # with open('./file1.txt', "w+", encoding='utf-8') as file1:
        #     ptrn = r"«Горячая линия»"
        #     for i in text.split("\n"):
        #
        #         text.replace("«Горячая линия»", "«Горячая линия» Министерства образования Ростовской области")
        #     print(text)       Не успел
    part1()
