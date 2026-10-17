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
#Этап 1. Разминка: переменные, числа, math
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


#if __name__ == "__main__":
    print("=== Этап 1: Разминка ===")
    
    print(f"Средняя оценка каталога: {average_rating(movies)}")
    print(f"Статистика возрастов (старый, новый, средний): {catalog_age_stats(movies)}")
    print(f"Длительность 'The Dune Chronicles' (155 мин): {duration_in_hours(movies[0]['duration_min'])}")

#Этап 2. Условия и match
def rating_tier(rating):
    """Возвращает категорию фильма по оценке, используя if/elif и тернарный оператор."""
    if rating >= 9:
        tier = "шедевр"
    elif rating >= 7:
        # Тернарный оператор здесь: если >= 8.9, то "хорошо (топ)", иначе просто "хорошо"
        # (это просто для выполнения условия задачи, на логику не влияет)
        tier = "хорошо (топ)" if rating >= 8.9 else "хорошо"
    elif rating >= 5:
        tier = "средне"
    else:
        tier = "слабо"
        
    return tier


def decade_label(year):
    """Возвращает метку десятилетия с использованием match и case _ if."""
    match year:
        case y if y > 2020:
            return "новые"
        case y if 2015 <= y <= 2020:
            return "недавние"
        case y if y < 2015:
            return "старые"
        case _:
            return "неизвестно" 
#Этап 3. Циклы
def print_non_comedy(movies):
    """Выводит названия фильмов, которые НЕ относятся к жанру comedy, используя for и continue."""
    print("Фильмы не в жанре 'comedy':")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue  # Пропускаем комедии
        print(f" - {movie['title']}")


def find_first_masterpiece(movies):
    """Находит первый фильм с рейтингом > 9.0, используя while и break."""
    index = 0
    found = False
    
    while index < len(movies):
        if movies[index]["rating"] > 9.0:
            print(f"Первый шедевр (рейтинг > 9.0): {movies[index]['title']} ({movies[index]['rating']})")
            found = True
            break  # Прерываем цикл, так как нашли
        index += 1
    
    if not found:
        # Эта ветка сработает, если мы прошли весь цикл и не наткнулись на break
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """Считает количество фильмов длиннее threshold минут через for с накоплением."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count
#if __name__ == "__main__":
    print("\n=== Этап 3: Циклы ===")
    # 1. Фильмы не-комедии
    print_non_comedy(movies)
    # 2. Поиск шедевра
    print("\nПоиск шедевра в каталоге:")
    find_first_masterpiece(movies)
        # Проверим случай, когда шедевра нет (передадим пустой список)
    print("\nПоиск шедевра в пустом каталоге:")
    find_first_masterpiece([])
        # 3. Подсчет длинных фильмов
    long_movies_count = count_long_movies(movies)
    print(f"\nКоличество фильмов длиннее 120 минут: {long_movies_count}")

#Этап 4. Строки
def normalize_title(title):
    """Приводит строку к Title Case без использования str.title()."""
    words = title.split()
    normalized_words = []
    
    for word in words:
        if word:  # Проверка на случай лишних пробелов
            # Делаем первую букву заглавной, остальные оставляем как есть (или можно .lower())
            norm_word = word[0].upper() + word[1:].lower()
            normalized_words.append(norm_word)
            
    return " ".join(normalized_words)


def make_slug(title):
    """Превращает название в слаг (например, 'silent-hours')."""
    # Сначала нормализуем (на всякий случай), затем в нижний регистр и меняем пробелы на дефисы
    norm_title = normalize_title(title)
    return norm_title.lower().replace(" ", "-")


def format_report_line(movie):
    """Возвращает единую строку с описанием фильма."""
    title = normalize_title(movie["title"]) 
    sorted_genres = sorted(list(movie["genres"]))
    genres_str = ", ".join(sorted_genres)
    duration_str = duration_in_hours(movie["duration_min"])
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration_str}, жанры: {genres_str}'
#if __name__ == "__main__":
    print("\n=== Этап 4: Строки ===")
    print(f"normalize_title: {normalize_title('silent hours')}")
    print(f"make_slug: {make_slug('Silent Hours')}")
    print(f"Строка отчета: {format_report_line(movies[7])}")

#Этап 5. Списки

def titles_sorted_by_rating(movies):
    """Возвращает список названий фильмов, отсортированных по убыванию рейтинга."""
    # Сортируем список фильмов по ключу 'rating' в обратном порядке.
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    
    # Собираем только названия в новый список
    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    """Возвращает список из n кортежей (title, rating) — топ по рейтингу."""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    
    # Берем первые n элементов с помощью среза и превращаем каждый в кортеж
    return [(movie["title"], movie["rating"]) for movie in sorted_movies[:n]]
#if __name__ == "__main__":
    print("\n=== Этап 5: Списки ===")
    print("Все фильмы по убыванию рейтинга:")
    print(titles_sorted_by_rating(movies))
    print("\nТоп-3 по рейтингу:")
    print(top_n_by_rating(movies, 3))

#Этап 6. Словари

def count_by_genre(movies):
    """Возвращает словарь {жанр: количество фильмов}, используя dict.get()."""
    genre_counts = {}
    
    for movie in movies:
        # В словаре movies жанры хранятся во множестве (set)
        for genre in movie["genres"]:
            # Если жанра нет, get вернет 0, и мы прибавим 1. Иначе прибавим 1 к текущему значению.
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
            
    return genre_counts


def actor_filmography(movies):
    """Возвращает словарь {актер: [список названий фильмов]}."""
    filmography = {}
    
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])      
    return filmography


def above_average_movies(movies):
    """Возвращает словарь {title: rating} для фильмов с рейтингом выше среднего, через dict comprehension."""
    # Получаем среднюю оценку каталога с помощью функции из Этапа 1
    avg = average_rating(movies)
    
    # Генератор словаря (dict comprehension)
    return {movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg}
#if __name__ == "__main__":
    print("\n=== Этап 6: Словари ===")
    print("Количество фильмов по жанрам:")
    print(count_by_genre(movies))
    print("\nФильмография актеров:")
    # Выведем для примера пару актеров
    actor_dict = actor_filmography(movies)
    print(f"O. Isaac: {actor_dict.get('O. Isaac')}")
    print(f"A. Novak: {actor_dict.get('A. Novak')}")
    print("\nФильмы с рейтингом выше среднего (средняя 7.2):")
    print(above_average_movies(movies))

#Этап 7. Множества

def all_genres(movies):
    """Возвращает множество всех уникальных жанров каталога."""
    genres = set()
    for movie in movies:
        # Используем оператор объединения
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    """Возвращает множество актеров, снимавшихся в обоих фильмах."""
    # Превращаем списки актеров во множества и берем пересечение
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    return actors1 & actors2


def genres_only_in_one(movies_a, movies_b):
    """Возвращает жанры, встречающиеся в movies_a, но не в movies_b."""
    # Собираем все жанры для первого списка фильмов
    genres_a = set()
    for movie in movies_a:
        genres_a |= movie["genres"]
        
    # Собираем все жанры для второго списка фильмов
    genres_b = set()
    for movie in movies_b:
        genres_b |= movie["genres"]
        
    # Возвращаем разность множеств
    return genres_a - genres_b
#if __name__ == "__main__":
    print("\n=== Этап 7: Множества ===")
    
    print("Все уникальные жанры в каталоге:")
    print(all_genres(movies))
    
    print("\nОбщие актеры в movies[0] и movies[3]:")
    print(common_actors(movies[0], movies[3]))
    
    print("\nЖанры только из movies[5:6], которых нет в movies[:5]:")
    print(genres_only_in_one(movies[5:6], movies[:5]))

#Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    """Генератор, который лениво отдает фильмы с рейтингом не ниже min_rating."""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def total_duration_high_rated(movies):
    """Возвращает суммарную длительность фильмов с рейтингом > 7 через генераторное выражение."""
    # Используем генераторное выражение (без квадратных скобок) внутри sum()
    return sum(m["duration_min"] for m in movies if m["rating"] > 7)
#if __name__ == "__main__":
    print("\n=== Этап 8: Итераторы и генераторы ===")
    print("Фильмы с рейтингом >= 8.0:")
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    print("\nСуммарная длительность фильмов с рейтингом > 7:")
    print(total_duration_high_rated(movies))

def build_report(movies):
    """Собирает и выводит единый консольный отчет по каталогу."""
    print("ОТЧЕТ ПО КАТАЛОГУ")
    
    # 1. Общая статистика
    avg_rating = average_rating(movies)
    # Берем средний возраст (третий элемент кортежа из Этапа 1)
    avg_age = catalog_age_stats(movies)[2] 
    
    print(f"Средний рейтинг: {avg_rating}")
    print(f"Средний возраст фильмов: {avg_age} лет")
    
    # 2. Топ-3 фильма
    print("\nТоп-3 фильма:")
    top_movies = top_n_by_rating(movies, n=3)
    for title, rating in top_movies:
        # Нам нужен полный объект фильма, чтобы передать его в format_report_line
        # Найдем его по названию
        movie_obj = next(m for m in movies if m["title"] == title)
        print(f"  {format_report_line(movie_obj)}")
        
    # 3. Фильмов по жанрам (сортировка по убыванию количества)
    print("\nФильмов по жанрам:")
    genres_count = count_by_genre(movies)
    # Сортируем по значению (количеству) по убыванию
    sorted_genres_count = sorted(genres_count.items(), key=lambda item: item[1], reverse=True)
    
    for genre, count in sorted_genres_count:
        print(f"  {genre} — {count}")
        
    # 4. Все жанры каталога (через запятую, по алфавиту)
    print("\nВсе жанры каталога:", end=" ")
    all_unique_genres = sorted(list(all_genres(movies)))
    print(", ".join(all_unique_genres))
if __name__ == "__main__":
    build_report(movies)