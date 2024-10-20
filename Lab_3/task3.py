
def count_letters(text):

    only_letters = []
    count_dict = {}

    for char in text.lower():
        if char.isalpha():
            only_letters.append(char)

    for char in only_letters:
        if char in count_dict.keys():
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict


def calculate_frequency(dict_):

    dict_frequency = {}

    for key, value in dict_.items():
        dict_frequency[key] = round(value / sum(dict_.values()), 2)

    return dict_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


dict_1 = count_letters(main_str)
dict_2 = calculate_frequency(dict_1)

for k, v in dict_2.items():
    print(f'{k}: {v:.2f}')

