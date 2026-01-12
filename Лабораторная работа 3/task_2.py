def find_common_participants(participants_first_group, participants_second_group, delimiter=','):

    first_set = set(part.strip() for part in participants_first_group.split(delimiter))
    second_set = set(part.strip() for part in participants_second_group.split(delimiter))

    common = first_set & second_set

    return sorted(list(common))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print(common)
