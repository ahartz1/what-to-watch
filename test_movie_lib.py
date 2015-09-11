from movie_lib import *


# all_users = []
# all_movies = []

siskel = User(5)
ebert = User(12)
# all_users[siskel.user_id] = siskel
# all_users[ebert.user_id] = ebert

movie1 = Movie(3, 'Toy Story')
movie2 = Movie(movie_id=9, movie_title='Pretty Woman')
# all_movies[movie1.movie_id] = movie1
# all_movies[movie2.movie_id] = movie2

rating1 = Rating(siskel.user_id, movie1.movie_id, stars=4)
rating2 = Rating(ebert.user_id, movie1.movie_id, stars=5)
rating3 = Rating(siskel.user_id, movie2.movie_id, stars=3)
# all_users[siskel.user_id].add_movie_rating(rating1)
# all_users[siskel.user_id].add_movie_rating(rating3)


def test_get_user_ratings():
    # Return a list of star ratings without user_ids
    assert len(all_movies[movie1.movie_id].get_user_ratings()) == 2


def test_get_movie_ratings():
    # Return a list of star ratings without movie_ids
    print(all_users[siskel.user_id])
    assert len(all_users[siskel.user_id].get_movie_ratings()) == 2
