def find_common_participants(group1: str, group2: str, delimiter: str = ",") -> list:#создаем функцию которая принимает две строки и разделяет их запятой

    participants1 = group1.split(delimiter) #делим строку на список участников
    participants2 = group2.split(delimiter)

    # Находим  общих участников
    common = set(participants1) & set(participants2)

    # оказывается есть функция котрая сортирует список в алфавитном порядк,я в шоке
    return sorted(common)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


result = find_common_participants(
    participants_first_group,
    participants_second_group,
    delimiter="|"
)

print(f"Общие участники: {result}")