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

    ratings = {}

    # use just (self, item_id, **kwargs)
    def __init__(self, movie_id, movie_title):
        self.movie_id = movie_id
        self.movie_title = movie_title
        all_movies[self.movie_id] = self


    def __str__(self):
        return 'Movie(movie_id: {}, movie_title: {})'.format(self.movie_id, repr(self.movie_title))


    def __repr__(self):
        return self.__str__()


    def add_rating(self, user_id, movie_id, stars):
        self.ratings[user_id] = stars


    def get_ratings(self):
        '''Returns list of all stars for this Movie'''
        return [r for _, r in self.ratings.items()]


    def ave_rating(self):
        return sum(self.get_ratings())/len(self.get_ratings())


    def get_ratings_with_id(self):
        return self.ratings.values()


class User:

    ratings = {}


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


    def add_rating(self, user_id, movie_id, stars):
        self.ratings[rating.movie_id] = stars


    def get_ratings(self):
        '''Returns list of all stars for this Movie'''
        return [r for _, r in self.ratings.items()]


    def ave_rating(self):
        return sum(self.get_ratings())/len(self.get_ratings())


    def get_ratings_with_id(self):
        return self.ratings.values()



class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = stars

        all_movies[self.movie_id].add_rating(self.user_id, self.movie_id, self.stars)

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

    # Find all stars for a movie by id
    movie_stars = movies[item_id].get_ratings()

    # Find the average rating for a movie by id
    movie_ave_rating = movies[item_id].ave_rating()

    # Find the name of a movie by id
    movie_title = movies[item_id].movie_title

    # Find all stars for a user
    user_stars = users[user_id].get_ratings()









if __name__ == '__main__':
    main()
