import random

movies = {
    'The Pursuit Of Happyness': ['drama', 'biography', 'motivational'],
    'Inception': ['sci-fi', 'thriller'],
    'Interstellar': ['sci-fi', 'drama', 'education'],
    'Conjuring': ['drama', 'horror'],
    'Gravity': ['sci-fi', 'thriller'],
    'The Shawshank Redemption': ['thriller', 'crime', 'inspirational'],
    'The Godfather': ['crime', 'drama'],
    'The Dark Knight': ['action', 'crime', 'drama'],
    'Schindler\'s List': ['biography', 'drama', 'history'],
    'Pulp Fiction': ['crime', 'drama'],
    'The Matrix': ['sci-fi', 'action'],
    'Forrest Gump': ['drama', 'romance', 'comedy'],
    'The Silence of the Lambs': ['thriller', 'crime', 'horror'],
    'Fight Club': ['drama', 'thriller'],
    'The Social Network': ['biography', 'drama'],
    'Parasite': ['thriller', 'drama'],
    'Mad Max: Fury Road': ['action', 'adventure', 'sci-fi'],
    'Toy Story': ['animation', 'adventure', 'comedy'],
    'Coco': ['animation', 'adventure', 'fantasy'],
    'The Lion King': ['animation', 'adventure', 'drama'],
    'The Grand Budapest Hotel': ['comedy', 'drama'],
    'A Beautiful Mind': ['biography', 'drama'],
    'Gladiator': ['action', 'adventure', 'drama'],
    'The Revenant': ['adventure', 'drama', 'thriller'],
    'La La Land': ['comedy', 'drama', 'music'],
    'Avatar': ['action', 'adventure', 'sci-fi'],
    'The Avengers': ['action', 'adventure', 'sci-fi'],
    'Black Panther': ['action', 'adventure', 'sci-fi'],
    'Joker': ['crime', 'drama', 'thriller'],
    'Titanic': ['drama', 'romance'],
}

def calculate_overlap(user_input, movie_features):
    return len(set(movie_features) & set(user_input.split()))

def recommend_movie(user_input, movies_data):
    matching_movies = []

    for movie, features in movies_data.items():
        if calculate_overlap(user_input, features) > 0:
            matching_movies.append(movie)

    if matching_movies:
        random.shuffle(matching_movies)
        return matching_movies[0]
    else:
        return None

while True:
    user_input = input("Enter your required/favorite genre: ")
    recommended_movie = recommend_movie(user_input, movies)

    if recommended_movie:
        print(f"Recommended movie for you: {recommended_movie}")
    else:
        print("Sorry, no recommendations found.")
