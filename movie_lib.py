'''
SUGGESTED CLASSES (one more)

Movie
movie id | movie title | release date | video release date |
IMDb URL | unknown | Action | Adventure | Animation |
Children's | Comedy | Crime | Documentary | Drama | Fantasy |
Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
Thriller | War | Western |

Use a dictionary for the genre?


User
user id | age | gender | occupation | zip code


Rating
Probably a subclass of Movie
Associates a particular user's rating of that movie


FUNCTIONS
Find all ratings for a movie by id
Find the average rating for a movie by id
Find the name of a movie by id
Find all ratings for a user

'''

class Movie:

    # use just (self, item_id, **kwargs)
    def __init__(self, item_id, movie_title, **kwargs):
    self.item_id = item_id
    self.movie_title = movie_title
    for key, value in kwargs.items():
        setattr(key, value)
    self.user_ratings = {}


class User:

    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        if 'age' in kwargs:
            self.age = kwargs['age']
        self.movie_ratings = {}


    def __str__(self):
        return 'User(id={})'.format(self.user_id)


    def __repr__(self):
        return self.__str__()


class Rating:

    def __init__(self, item_id, user_id, rating):
        self.item_id = item_id
        self.user_id = user_id
        self.rating = rating



users = {}
movies = {}












#
