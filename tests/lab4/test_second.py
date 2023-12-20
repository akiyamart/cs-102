import unittest
import sys
import os
sys.path.append('D:\Vscode\studying\cs-102')
from src.lab4.task2.main import AgeGroupsManager, SurveyParticipant, AgeGroup, input_file

class TestAgeGroupsManager(unittest.TestCase):

    def setUp(self):
        self.age_boundaries = [15, 22, 30, 50]
        self.age_groups_manager = AgeGroupsManager(self.age_boundaries)
        self.age_groups_manager.read_participants_from_file(input_file)
    def test_read_participants_from_file(self):

        expected_result = [
            '31-50: Петров Петр Петрович (35)',
            '23-30: Иванов Иван Иванович (25)',
            '16-22: Сидоров Сидор Сидорович (18)',
            '0-15: Абдулаев Коля Абдулаевич (12)'
        ]
        self.assertEqual(self.age_groups_manager.get_age_groups_info(), expected_result)

if __name__ == '__main__':
    unittest.main()
