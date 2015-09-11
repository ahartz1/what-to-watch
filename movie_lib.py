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
    def __init__(self, item_id, movie_title=None, **kwargs):
        self.item_id = item_id
        self.movie_title = movie_title
        # for key, value in kwargs.items():
        #     setattr(key, value)
        self.user_ratings = {}


    def __str__(self):
        return 'Movie(item_id: {}, movie_title: {})'.format(self.item_id, self.movie_title)


    def __repr__(self):
        return self.__str__()


    def ratings(self):
        '''Returns list of all ratings for this Movie'''
        ret = []
        for _, u_rating in self.user_ratings.items():
            ret.append(u_rating)
        return ret


    def ave_rating(self):
        return sum(self.ratings())/len(self.ratings())


    def add_rating(self, user_id, rating):
        self.user_ratings[user_id] = rating


    def add_title(self, title):
        self.movie_title = title


class User:

    def __init__(self, user_id, **kwargs):
        self.user_id = user_id
        # if 'age' in kwargs:
        #     self.age = kwargs['age']
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

    def movie(self):
        pass


def main():
    data_list = []
    item_list = []
    user_list = []
    users = {}
    movies = {}

    ''' 1. Read u.data into master_list, close file; for each entry,
            a. Check if a movie is in movies
                - if not in movies, create a new Movie with just the item_id and
                    add the user_id and rating as an entry in its ratings dictionary
                - if it is in movies, add the user_id and rating as an entry in its
                    ratings dictionary
        2. Read u.item into item_list
            a. For each movie in movies, populate attributes
        3. Read u.user into user_list, populate users dictionary
    '''

    # Find all ratings for a movie by id
    movie_ratings = movies[item_id].ratings()

    # Find the average rating for a movie by id
    movie_ave_rating = movies[item_id].ave_rating()

    # Find the name of a movie by id


    # Find all ratings for a user










if __name__ == '__main__':
    main()
