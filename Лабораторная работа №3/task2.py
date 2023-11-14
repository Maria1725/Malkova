# TODO Напишите функцию find_common_participants
def find_common_participants(pervaya, vtoraya, b=','):
    a = set(pervaya.split(b)).intersection(vtoraya.split(b))
    a = list(a)
    a.sort()
    return a


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, b='|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
