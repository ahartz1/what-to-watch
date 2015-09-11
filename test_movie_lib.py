from movie_lib import *
# from nose.tools import raises


def is_equal(x, y, tolerance=0.001):
    """Helper function to compare floats, which are often not quite equal
    even when they should be."""
    return abs(x - y) <= tolerance


# data_list = []
# item_list = []
# user_list = []


users = {14: User(14), 62: User(62), 23: User(23)}
movies = {6: Movie(6), 72: Movie(72), 3: Movie(3)}
movies[6].add_rating(14, 3)
movies[3].add_rating(14, 4)
movies[3].add_rating(62, 3)
movies[3].add_rating(23, 3)
movies[3].add_title('The Last of the Mohecians')
users[14].add_rating(6, 3)
users[14].add_rating(3, 4)
users[62].add_rating(3, 3)
users[23].add_rating(3, 3)



def test_retrieve_ratings():
    '''Tests the get_ratings method for the Movie class'''
    assert movies[72].get_ratings() == []


def test_movie_add_rating():
    '''Tests the add_rating method for the Movie class'''
    assert movies[6].get_ratings() == [3]


def test_movie_ave_rating():
    '''Tests the ave_rating method for the Movie class'''
    assert movies[3].ave_rating() == 10/3


def test_movie_add_title():
    '''Tests the add_title method in Movie class'''
    assert movies[3].movie_title == 'The Last of the Mohecians'


def test_user_add_rating():
    '''Tests the add_rating method for the User class'''
    assert users[23].ratings[3] == 3


def test_user_get_ratings():
    '''Tests the get_ratings method for the User class'''
    assert users[23].get_ratings() == [3]


def test_user_get_ratings_with_id():
    '''Tests the get_ratings_with_id method for the Users class'''
    assert users[14].get_ratings_with_id() == [[3, 4], [6, 3]]
