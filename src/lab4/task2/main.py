import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, 'input_resp.txt')
import os

class SurveyParticipant:
    """Класс для представления участника опроса."""
    def __init__(self, name, age):
        """Инициализация участника опроса."""
        self.name = name
        self.age = age

    def __lt__(self, other):
        """Сравнение участников опроса."""
        return (self.age, self.name) > (other.age, other.name)

    def __str__(self):
        """Строковое представление участника опроса."""
        return f"{self.name} ({self.age})"


class AgeGroup:
    """Класс для представления возрастной группы."""
    def __init__(self, name, min_age, max_age):
        """Инициализация возрастной группы."""
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.participants = []

    def add_participant(self, participant):
        """Добавление участника в возрастную группу."""
        self.participants.append(participant)

    def __str__(self):
        """Строковое представление возрастной группы."""
        participants_info = ', '.join(str(participant) for participant in sorted(self.participants))
        return f"{self.name}: {participants_info}"


class AgeGroupsManager:
    """Класс для управления возрастными группами."""
    def __init__(self, boundaries):
        """Инициализация управляющего класса."""
        self.groups = [
            AgeGroup(f"{boundaries[i - 1] + 1}-{boundaries[i]}", boundaries[i - 1] + 1, boundaries[i])
            for i in range(len(boundaries) - 1, 0, -1)
        ]
        self.groups.append(AgeGroup(f"0-{boundaries[0]}", 0, boundaries[0]))
        self.groups.append(AgeGroup(f"{boundaries[-1] + 1}+", boundaries[-1] + 1, float('inf')))

    def add_participant(self, participant):
        """Добавление участника в соответствующую возрастную группу."""
        for group in self.groups:
            if group.min_age <= participant.age <= group.max_age:
                group.add_participant(participant)
                break

    def get_age_groups_info(self):
        """Получение информации о возрастных группах."""
        sorted_groups = sorted(self.groups, key=lambda x: x.min_age, reverse=True)
        return [str(group) for group in sorted_groups if group.participants]

    def read_participants_from_file(self, file_path):
        """Чтение участников из файла и добавление их в соответствующие возрастные группы."""
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip() == "END":
                    break
                else:
                    name, age = line.strip().split(',')
                    participant = SurveyParticipant(name, int(age))
                    self.add_participant(participant)


if __name__ == "__main__":
    age_boundaries = list(map(int, input('Введите возрастные границы:').split()))
    age_groups_manager = AgeGroupsManager(age_boundaries)
    age_groups_manager.read_participants_from_file(input_file)
    age_groups_info = age_groups_manager.get_age_groups_info()
    for group_info in age_groups_info:
        print(group_info)
