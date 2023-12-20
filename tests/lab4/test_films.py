import unittest
import sys
sys.path.append('D:\Vscode\studying\cs-102')
from src.lab4.task1.main import movies_file_path, views_file_path
from src.lab4.task1.main import MovieRecommendationSystem, Movie

class TestMovieRecommendationSystem(unittest.TestCase):

    def setUp(self):
        self.recSystem = MovieRecommendationSystem(movies_file_path, views_file_path)

    def test_get_views(self):
        self.assertEqual(self.recSystem.recommend_movie([2,4]), 'Дюна')
        self.assertEqual(self.recSystem.recommend_movie([1,5,6]), None)
        self.assertEqual(self.recSystem.recommend_movie([1,3,4]), 'Хатико')
        self.assertEqual(self.recSystem.recommend_movie([3]), 'Мстители: Финал')

if __name__ == '__main__':
    unittest.main()
