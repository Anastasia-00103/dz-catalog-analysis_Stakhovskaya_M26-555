import math
movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
] 
def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, округленную до одного знака."""
    if not movies:
        return 0.0
    
    total_rating = sum(movie["rating"] for movie in movies)
    avg = total_rating / len(movies)
    return round(avg, 1)


def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж: (самый старый возраст, самый новый возраст, средний возраст)."""
    if not movies:
        return (0, 0, 0)
    
    # Вычисляем возраст каждого фильма
    ages = [current_year - movie["year"] for movie in movies]
    
    oldest = max(ages)
    newest = min(ages)
    
    # Среднее арифметическое возрастов, округленное вверх
    avg_age = math.ceil(sum(ages) / len(ages))
    
    # Возвращаем кортеж (tuple)
    return (oldest, newest, avg_age)

def duration_in_hours(minutes):
    """Переводит минуты в формат 'Xч Yм', используя // и %."""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


if __name__ == "__main__":
    print("=== Этап 1: Разминка ===")
    
    print(f"Средняя оценка каталога: {average_rating(movies)}")
    print(f"Статистика возрастов (старый, новый, средний): {catalog_age_stats(movies)}")
    print(f"Длительность 'The Dune Chronicles' (155 мин): {duration_in_hours(movies[0]['duration_min'])}") 
