from other_movie_lib import *


siskel = User(5)
ebert = User(12)
movie1 = Movie(3, 'Toy Story')
movie2 = Movie(9, 'Pretty Woman')

all_movies = [movie1, movie2]

def test_find_ratings_for_movie():
    # toy_story_ratings = get_ratings_for_movie(movie1.id)

    # Return a list of Rating objects
    toy_story_ratings = all_movies[movie1.id].get_ratings()
