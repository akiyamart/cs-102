import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
movies_file_path = os.path.join(BASE_DIR, 'movies.txt')
views_file_path = os.path.join(BASE_DIR, 'views.txt')

class Movie:
    """Класс для представления фильма."""
    def __init__(self, movie_id, title):
        """Инициализация фильма."""
        self.movie_id = movie_id
        self.title = title

    def __str__(self):
        """Строковое представление фильма."""
        return f"{self.movie_id}, {self.title}"

class MovieRecommendationSystem:
    """Система рекомендации фильмов."""
    def __init__(self, movies_filename, views_filename):
        """Инициализация системы."""
        self.movies = self.load_movies(movies_filename)
        self.views = self.load_views(views_filename)

    def load_movies(self, filename):
        """Загрузка данных о фильмах."""
        movies = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                movie_id, title = line.strip().split(',')
                movies.append(Movie(int(movie_id), title))
        return movies

    def load_views(self, filename):
        """Загрузка данных о просмотрах."""
        views = []
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                views.append(list(map(int, line.strip().split(','))))
        return views

    def recommend_movie(self, user_views):
        """Рекомендация фильма на основе просмотров пользователя."""
        matching_users = self.find_matching_users(user_views)
        remaining_movies = self.find_remaining_movies(user_views, matching_users)
        recommended_movie = self.choose_recommended_movie(remaining_movies)
        return recommended_movie.title if recommended_movie else None

    def find_matching_users(self, user_views):
        """Поиск пользователей с похожей историей просмотров."""
        matching_users = []
        for i, views in enumerate(self.views):
            common_views = set(user_views) & set(views)
            if len(common_views) >= len(user_views) / 2:
                matching_users.append(i)
        return matching_users

    def find_remaining_movies(self, user_views, matching_users):
        """Поиск непросмотренных фильмов, просмотренных похожими пользователями."""
        viewed_movies = set(user_views)
        remaining_movies = []
        for i in matching_users:
            remaining_movies.extend(set(self.views[i]) - viewed_movies)
        return list(set(remaining_movies))

    def choose_recommended_movie(self, remaining_movies):
        """Выбор рекомендованного фильма на основе количества просмотров."""
        movie_counts = {}
        for movie_id in remaining_movies:
            users_watched = set()
            for i, views in enumerate(self.views):
                if movie_id in views:
                    users_watched.add(i)

            movie_counts[movie_id] = len(users_watched)

        if not movie_counts:
            return None

        max_count = max(movie_counts.values())
        top_movies = [movie_id for movie_id, count in movie_counts.items() if count == max_count]
        return self.movies[top_movies[0] - 1] if top_movies else None

if __name__ == "__main__":
    recommendation_system = MovieRecommendationSystem(movies_file_path, views_file_path)

    while True:
        try:
            user_input = input("Введите историю просмотров через запятую: ")
            user_history = list(map(int, user_input.split(',')))

            if user_history:
                break
            else:
                print("Пожалуйста, введите хотя бы один элемент.")
        except ValueError:
            print("Некорректный ввод")

    recommended_film = recommendation_system.recommend_movie(user_history)

    print(f"Рекомендуемый фильм: {recommended_film}")

