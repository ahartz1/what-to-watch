import csv
import math


all_movies = {}
all_users = {}


class Movie:
    # use just (self, item_id, **kwargs)
    def __init__(self, id, title):
        self.id = int(id)
        self.title = title
        all_movies[self.id] = self
        self.user_ratings = {}

    def __str__(self):
        return 'Movie(id: {}, title: {})'.format(self.id, repr(self.title))

    def __repr__(self):
        return self.__str__()

    def add_user_rating(self, rating):
        self.user_ratings[rating.user_id] = rating.stars

    def get_user_ratings(self):
        '''Returns list of user ratings of this Movie'''
        return [r for _, r in self.user_ratings.items()]

    def get_user_ratings_w_movie_id(self):
        '''Returns dict of user_id and their associated ratings of this Movie'''
        return self.user_ratings.values()

    def ave_user_rating(self):
        u_r = self.get_user_ratings()
        return sum(u_r)/len(u_r)

    def num_user_ratings(self):
        return len(self.get_user_ratings())


class User:
    def __init__(self, id):
        self.id = int(id)
        self.movie_ratings = {}
        # if 'age' in kwargs:
        #     self.age = kwargs['age']
        all_users[self.id] = self

    def __str__(self):
        return 'User(id={})'.format(self.id)

    def __repr__(self):
        return self.__str__()

    def add_movie_rating(self, rating):
        self.movie_ratings[rating.movie_id] = rating.stars

    def get_movie_ratings(self):
        '''Returns list of all star ratings user has applied'''
        return [r for _, r in self.movie_ratings.items()]

    def get_movie_ids(self):
        '''Returns list containing movie_id for each movie in user's dict'''
        return [m_id for m_id, _ in self.movie_ratings.items()]

    def get_movie_data(self):
        '''Returns list of (movie_id, rating) tuples for each movie in user's dict'''
        return [(m_id, r) for m_id, r in self.movie_ratings.items()]

    def get_overlaps(self, movie_data_list):
        common_movies = []
        for x_m in movie_data_list:
            if x_m[0] in self.get_movie_ids():
                common_movies.append((x_m[0], self.movie_ratings[x_m[0]]))
        return common_movies

    def ave_movie_rating(self):
        m_r = self.get_movie_ratings()
        return sum(m_r)/len(m_r)


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = int(stars)
        all_movies[self.movie_id].add_user_rating(self)
        all_users[self.user_id].add_movie_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(self.user_id, self.movie_id, self.stars)

    def __repr__(self):
        return self.__str__()


def init_structures():
    '''Create Movie, User, and Ratings objects from data in MovieLens files'''

    # Create a Movie object for each line of u.item
    with open('u.item', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['id', 'title'], delimiter='|')
        for row in reader:
            Movie(int(row['id']), row['title'])

    # Create a User object for each line in u.user
    with open('u.user', encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=['id'], delimiter='|')
        for row in reader:
            User(int(row['id']))

    # Create a Rating object for each line in u.data
    with open ('u.data') as f:
         reader = csv.DictReader(f, fieldnames=['user_id', 'movie_id', 'stars'], delimiter='\t')
         for row in reader:
              Rating(int(row['user_id']), int(row['movie_id']), int(row['stars']))


def pop_movies(num_results, min_ratings=95):
    ret = sorted([(m.title, m.ave_user_rating()) for m_id, m in all_movies.items() if m.num_user_ratings() > min_ratings], key=lambda c: c[1], reverse=True)[:num_results]
    return [m[0] for m in ret]


def pop_movies_for_user(user_id, num_results, min_ratings=95):
    ret = sorted([(m.title, m.ave_user_rating())
                 for m_id, m in all_movies.items()
                 if m.num_user_ratings() > min_ratings and m_id not in all_users[user_id].get_movie_ids()
                 ], key=lambda c: c[1], reverse=True)[:num_results]
    return [m[0] for m in ret]


def similar_users(my_user_id):
    '''Return list of [user_id, euclidean_distance] sorted by most similar'''

    '''1. Get list of my_user_id's movies and ratings'''
    my_list = all_users[my_user_id].get_movie_data()

    '''2. Iterate through all_users[u_id].movie_ratings.items() and get the list
          of movies in common with my_user_id.'''
    user_lists = [all_users[u_id].get_overlaps(my_list) for u_id, _ in all_users.items()]

    similar_list = sorted([(u_id, euclidean_distance(my_list, all_users[u_id].get_movie_ids()))
           for u_id, _ in all_users.items()
           ], key=lambda c: c[1], reverse=True)
    return similar_list


def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """
    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))


def main():
    print('Initializing data structures from MovieLens data files . . .')
    init_structures()
    print('Initialization complete.\n')

    # There are 141 movies with just 1 user rating.

    # print(pop_movies(20, 200))
    # print('Top 30 most popular movies with over 200 ratings:')
    # [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(pop_movies(30,200))]

    # print('Top 20 most popular movies with over 200 ratings that user 399 has not seen:')
    # # print(pop_movies_for_user(399, 20, 200))
    # [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(pop_movies_for_user(399,20,200))]
    #
    # print('\n List of all movie_ids that user 399 has rated:')
    # print(all_users[399].movie_ratings.items())

    print('\nTop 20 users similar to user 399:')
    [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(similar_users(399)[:20])]


if __name__ == '__main__':
    main()
