
def find_common_participants(group_1, group_2, sep=','):
    group_1_set = set(group_1.split(sep))
    group_2_set = set(group_2.split(sep))

    union = list(group_2_set.intersection(group_1_set))
    union.sort()

    return union

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print('Общие:', find_common_participants(participants_first_group, participants_second_group, '|'))
