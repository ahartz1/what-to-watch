from movie_lib import *


siskel = User(5)
ebert = User(11)

movie1 = Movie(4, 'Big')
movie2 = Movie(8, 'The Blob')
movie3 = Movie(6, "Howard's End")

rating1 = Rating(siskel.id, movie1.id, stars=2)
# rating2 = Rating(ebert.id, movie1.id, stars=4)
rating3 = Rating(siskel.id, movie2.id, stars=1)
rating4 = Rating(ebert.id, movie2.id, stars=5)
rating5 = Rating(siskel.id, movie3.id, stars=3)

def test_user_creation():
    siskel = User(5)
    ebert = User(11)
    assert siskel.id == 5
    assert ebert.id == 11


def test_movie_creation():
    movie1 = Movie(4, 'Big')
    movie2 = Movie(8, 'The Blob')
    assert movie1.id == 4
    assert movie1.title == 'Big'
    assert movie2.id == 8
    assert movie2.title == 'The Blob'


def test_rating_creation():
    rating1 = Rating(siskel.id, movie1.id, stars=2)
    rating2 = Rating(ebert.id, movie1.id, stars=4)
    rating3 = Rating(siskel.id, movie2.id, stars=1)
    rating4 = Rating(ebert.id, movie2.id, stars=5)


def test_get_user_ratings():
    # Return a list of star ratings without user_ids
    assert sorted(all_movies[movie1.id].get_user_ratings()) == [2, 4]


def test_get_movie_ratings():
    # Return a list of star ratings without movie_ids
    assert sorted(all_users[siskel.id].get_movie_ratings()) == [1, 2]


def test_ave_user_rating():
    assert all_movies[movie1.id].ave_user_rating() == 3


def test_get_overlaps():
    assert siskel.get_overlaps(ebert.get_movie_data()) == [(8, 1)]
