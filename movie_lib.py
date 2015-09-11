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


class Rating:

    def __init__(self, id, ratings={}):
        self.id = id
        self.ratings = {}


    def add_rating(self, id, rating):
        self.ratings[id] = rating


    def get_ratings(self):
        '''Returns list of all ratings for this Movie'''
        return [r for _, r in self.ratings.items()]


    def ave_rating(self):
        return sum(self.get_ratings())/len(self.get_ratings())


    def get_ratings_with_id(self):
        print([[i, r] for i, r in self.ratings.items()])
        return [[i, r] for i, r in self.ratings.items()]


class Movie(Rating):

    # use just (self, item_id, **kwargs)
    def __init__(self, id, movie_title=None, ratings={}, **kwargs):
        super().__init__(id, ratings)
        self.movie_title = movie_title
        # for key, value in kwargs.items():
        #     setattr(key, value)
        # self.user_ratings = {}


    def __str__(self):
        return 'Movie(id: {}, movie_title: {})'.format(self.id, self.movie_title)


    def __repr__(self):
        return self.__str__()


    def add_title(self, title):
        self.movie_title = title


class User(Rating):

    def __init__(self, id, ratings={}, **kwargs):
        super().__init__(id, ratings)
        # if 'age' in kwargs:
        #     self.age = kwargs['age']
        # self.movie_ratings = {}


    def __str__(self):
        return 'User(id={})'.format(self.id)


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
                    add the user_id and rating as an entry in its ratings dictionary
                - if it is in movies, add the user_id and rating as an entry in its
                    ratings dictionary
        2. Read u.item into item_list
            a. For each movie in movies, populate attributes
        3. Read u.user into user_list, populate users dictionary
    '''

    # Find all ratings for a movie by id
    movie_ratings = movies[item_id].get_ratings()

    # Find the average rating for a movie by id
    movie_ave_rating = movies[item_id].ave_rating()

    # Find the name of a movie by id
    movie_title = movies[item_id].movie_title

    # Find all ratings for a user
    user_ratings = users[user_id].get_ratings()









if __name__ == '__main__':
    main()
