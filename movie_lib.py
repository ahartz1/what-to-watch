'''
SUGGESTED CLASSES

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
A parent class of Movie and User
Provides a place to collect id, rating pairs.
'''
import csv


all_movies = {}
all_users = {}


class Movie:

    user_ratings = {}

    # use just (self, item_id, **kwargs)
    def __init__(self, movie_id, movie_title):
        self.movie_id = movie_id
        self.movie_title = movie_title
        all_movies[self.movie_id] = self


    def __str__(self):
        return 'Movie(movie_id: {}, movie_title: {})'.format(self.movie_id, repr(self.movie_title))


    def __repr__(self):
        return self.__str__()


    def add_user_rating(self, rating):
        self.user_ratings[rating.user_id] = rating.stars


    def get_user_ratings(self):
        '''Returns dictionary of users and their ratings of this Movie'''
        return [r for _, r in self.user_ratings.items()]


    def ave_rating(self):
        return sum(self.get_user_ratings())/len(self.get_user_ratings())


    def get_user_ratings_with_id(self):
        return self.user_ratings.values()


class User:


    movie_ratings = {}


    def __init__(self, user_id):
        self.user_id = user_id
        # if 'age' in kwargs:
        #     self.age = kwargs['age']
        # self.movie_stars = {}
        all_users[self.user_id] = self


    def __str__(self):
        return 'User(user_id={})'.format(self.user_id)


    def __repr__(self):
        return self.__str__()


    def add_movie_rating(self, rating):
        self.movie_ratings[rating.movie_id] = rating.stars


    def get_movie_ratings(self):
        '''Returns list of all stars for this Movie'''
        return [r for _, r in self.movie_ratings.items()]


    def ave_movie_rating(self):
        return sum(self.get_movie_ratings())/len(self.get_movie_ratings())


    def get_movie_ratings_with_user_id(self):
        return self.movie_ratings.values()



class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_user_rating(self)
        all_users[self.user_id].add_movie_rating(self)


    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)


    def __repr__(self):
        return self.__str__()


def main():
    data_list = []
    item_list = []
    user_list = []
    users = {}
    movies = {}

    ''' 1. Read u.data into master_list, close file; for each entry,
            a. Check if a movie is in movies
                - if not in movies, create a new Movie with just the item_id and
                    add the user_id and rating as an entry in its stars dictionary
                - if it is in movies, add the user_id and rating as an entry in its
                    stars dictionary
        2. Read u.item into item_list
            a. For each movie in movies, populate attributes
        3. Read u.user into user_list, populate users dictionary
    '''


    with open('~/TIY/ml-100k/u.item', encoding='latin_1') as f:
         reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title'] delimiter='|')
         for row in reader:
              print(row)


    with open('~/TIY/ml-100k/u.user', encoding='latin_1') as f:
         reader = csv.DictReader(f, fieldnames=['movie_id', 'movie_title'] delimiter='|')
         for row in reader:
              print(row)


    with open ('~/TIY/ml-100k/u.data') as f:
         reader = cvs.DictReader(f, delimiter='|')
         for row in reader:
              print(row)








if __name__ == '__main__':
    main()
