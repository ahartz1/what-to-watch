from other_movie_lib import *


siskel = User(5)
ebert = User(12)
movie1 = Movie(movie_id=3, movie_title='Toy Story')
movie2 = Movie(movie_id=9, movie_title='Pretty Woman')
rating1 = Rating(siskel.user_id, movie1.movie_id, stars=4)
rating2 = Rating(ebert.user_id, movie1.movie_id, stars=5)

all_movies[movie1.movie_id] = movie1
all_movies[movie2.movie_id] = movie2


def test_find_ratings_for_movie():
    # toy_story_ratings = get_ratings_for_movie(movie1.id)

    # Return a list of Rating objects
    all_movies[movie1.movie_id].get_ratings() == [4, 5]
