import csv
import math
from os import get_terminal_size

all_movies = {}
all_users = {}


class Movie:
    # use just (self, item_id, **kwargs)
    def __init__(self, id, title):
        self.id = int(id)           # This movie's id
        self.title = title          # This movie's title
        all_movies[self.id] = self  # Add this movie to global all_movies dictionary
        self.user_ratings = {}      # Dictionary of this movie's user ratings

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
        self.id = int(id)           # This user's id
        self.movie_ratings = {}     # Dict of this user's movie ratings
        self.similars = []
        # [[other_user_id, euclidean_distance, [[com_mov, rat], ...]], ...]

        self.min_overlap = None     # Similar overlap used in generating similars
        self.recommendations = {}   # {movie_id: [rat]}

        # if 'age' in kwargs:
        #     self.age = kwargs['age']

        all_users[self.id] = self   # Add user to global all_users dictionary

    def __str__(self):
        return 'User(id={})'.format(self.id)

    def __repr__(self):
        return self.__str__()

    def add_movie_rating(self, rating):
        self.movie_ratings[rating.movie_id] = rating.stars

    def ave_movie_rating(self):
        m_r = self.get_movie_ratings()
        return sum(m_r)/len(m_r)

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
        return sorted(common_movies)

    def comparison_list_maker(self, overlap_list):
        '''For overlapping movies, outputs a list with two ratings lists: one
           for self and one for the user_id represented by the overlap_list'''
        u_ratings = []
        o_ratings = []
        for m_id, r in self.movie_ratings.items():
            for o_r in overlap_list:
                if m_id == o_r[0]:
                    u_ratings.append(r)
                    o_ratings.append(o_r[1])
        return u_ratings, o_ratings

    def high_to_low(self):
        return [(i+1, m[1], all_movies[m[0]].title)
                for i, m in enumerate(
                sorted(self.get_movie_data(), key=lambda c: c[1], reverse=True))]

    def get_rec_ids(self):
        return [m for m, r in self.recommendations.items()]


class Rating:
    def __init__(self, user_id, movie_id, stars):
        self.user_id = user_id
        self.movie_id = movie_id
        self.stars = int(stars)
        all_movies[self.movie_id].add_user_rating(self)
        all_users[self.user_id].add_movie_rating(self)

    def __str__(self):
        return 'Rating(user_id={}, movie_id={}, stars={})'.format(
                self.user_id, self.movie_id, self.stars)

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
    ret = sorted([(m.title, m.ave_user_rating())
                 for m_id, m in all_movies.items()
                 if m.num_user_ratings() > min_ratings],
                 key=lambda c: c[1], reverse=True)[:num_results]
    return [m[0] for m in ret]


def pop_movies_for_user(user_id, num_results, min_ratings=95):
    ret = sorted([(m.title, m.ave_user_rating())
                 for m_id, m in all_movies.items()
                 if m.num_user_ratings() > min_ratings and m_id not in all_users[user_id].get_movie_ids()
                 ], key=lambda c: c[1], reverse=True)[:num_results]
    return [m[0] for m in ret]


def similar_users(my_user_id, min_overlap=15):
    '''Return list of [user_id, euclidean_distance] sorted by most similar'''
    my_user = all_users[my_user_id]

    my_list = sorted(my_user.get_movie_data())
    my_movie_ids = my_user.get_movie_ids()

    '''Associate each user_id with a list of get_overlaps with my_user_id'''
    user_lists = [(u_id, u.get_overlaps(my_list))
                  for u_id, u in all_users.items()
                  if u_id != my_user_id]

    '''For each item in user_lists, make list of two lists: one for my_user_id
       and one for the user represented in the user_lists element'''

    user_similarity_list = []
    # Holds [[user_id, euclidean_distance, [[com_mov, rat], ...], min_overlap], ...]

    for u_list in user_lists:
        if len(u_list[1]) >= min_overlap:
            euclid_prep_user = []
            euclid_prep_other = []
            for m in u_list[1]:
                if m[0] in my_movie_ids:
                    euclid_prep_other.append(m[1])
                    euclid_prep_user.append(my_user.movie_ratings[m[0]])
            user_similarity_list.append([
                u_list[0], # corresponds to user_id
                euclidean_distance(euclid_prep_user, euclid_prep_other),
                u_list[1] # corresponds to [[common_movie_id_1, rating_1], ... ]
                ]) #TODO: Caller store in my_user_id for future use
    if len(user_similarity_list) > 0:
        my_user.min_overlap = min_overlap
    return sorted(user_similarity_list, key=lambda c: c[1], reverse=True)


def recs_by_taste(my_user_id, min_overlap=15):
    '''Returns list of all movie titles and their weighted ratings'''

    user = all_users[my_user_id]
    my_viewed_movies = user.get_movie_ids()

    # If no user doesn't have an existing recommendation list, create one OR
    # If user has existing recommendation list, but of the wrong overlap, replace it.
    if len(user.similars) == 0 or my_user.min_overlap != min_overlap:
        user.similars = similar_users(my_user_id, min_overlap)

    for s_user in user.similars: # o_user is for "similar user"
        for m_id, r in all_users[s_user[0]].movie_ratings.items():
            if m_id not in my_viewed_movies:
                if m_id in user.get_rec_ids():
                    if user.recommendations[m_id] < s_user[1]*r:
                        user.recommendations[m_id] = s_user[1]*r
                else:
                    user.recommendations[s_user[0]] = s_user[1]*r
    ret = [[all_movies[m_id].title, r] # movie title, anticipated user rating
            for m_id, r in user.recommendations.items()]
    return [[m[0], m[1]] for m in sorted(ret, key=lambda c: c[1], reverse=True)]


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


def print_welcome(width, height):
    print('_'*width)
    vertical_bars = '|'+''.center(width-2)+'|'
    print((vertical_bars+'\n')*3+vertical_bars)
    print('|'+'What to Watch'.upper().center(width-2)+'|')
    print(vertical_bars)
    print('|'+'Movie Recommendation Engine'.center(width-2)+'|')
    print((vertical_bars+'\n')*4+vertical_bars)
    print('|  '+'The MovieLens 100k database working for you!'.ljust(width-4)+'|')
    print((vertical_bars+'\n')*2+vertical_bars)
    print('—'*width+'\n'*2)
    print('\n'*(height-21-6))


def print_popular(num_results=20, num_raters=200):
    [print('{:' '>3}: {}'.format(i+1, m))
     for i, m in enumerate(pop_movies(num_results, num_raters))]


def print_popular_for_user(user_id, num_results, num_raters):
        [print('{:' '>3}: {}'.format(i+1, m))
               for i, m in enumerate(
               pop_movies_for_user(user_id, num_results, num_raters))]

def print_recs_by_taste(user_id, num_results, width, height, min_overlap=15):
    rec_results = []
    max_title = 0
    print('\nCalculating your results . . .\n')
    rec_results = recs_by_taste(user_id, min_overlap)
    print('\nTop {} recommendations for user {}:\n'.format(num_results, user_id))

    # Calculate table width
    for m in rec_results[:num_results]:
        if len(m[0]) > max_title:
            max_title = len(m[0])
    table_width = 15 + max_title
    if table_width > width:
        table_width = width
    print('Rank | Corr  | Movie Title')
    print('—'*table_width)
    [print('{:4d}: ({:.2f}) | {}'.format(i+1, m[1], m[0]))
           for i, m in enumerate(rec_results[:num_results])]
    vertical_padding = height - num_results - 8
    if vertical_padding > 0:
        print('\n'*vertical_padding)


def get_user_id():
    while True:
        user_id = input('userID> ')
        if user_id.isdigit():
            if 1 <= int(user_id) <= 943:
                return int(user_id)
        elif user_id == '':
            return ''
        else:
            continue


def main():
    width = 80          # default width
    height = 24         # default height
    terminal_info = {}  # dictionary to receive terminal info from system
    mode = None         # variable to hold recommendation mode
    user_id = None      # variable to hold user_id of user

    terminal_info = get_terminal_size()
    if terminal_info[0] > 0:
        width = terminal_info[0]
    if terminal_info[1] > 0:
        height = terminal_info[1]

    print('Initializing data structures from MovieLens files . . . ', end='')
    init_structures()
    print('complete.\n')

    print_welcome(width, height)

    print('To see recommendations based on your preferences, please enter your '
          'userID.\nOtherwise, press Enter to browse the most popular movies in '
          'the database.')

    user_id = get_user_id()

    #TODO: mode loops
    if user_id == '':
        print('\n'*2+'Here are the top 20 most popular movies with over 200 '
              'ratings:'+'\n'*2)
        print_popular()
        # print('\n'*2+'To see more results, press Enter.')
    else:
        print_recs_by_taste(user_id, 20, width, height, 8)
        # print('\nTop 20 recommendations for userID {}:\n'.format(user_id))
        # [print('{:3d}: sim: {:.2f} | {}'.format(i+1, m[1], m[0]))
        #        for i, m in enumerate(recs_by_taste(user_id)[:20])]
    # There are 141 movies with just 1 user rating.

    # print(pop_movies(20, 200))
    # print('Top 30 most popular movies with over 200 ratings:')
    # [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(pop_movies(30,200))]

    # print('\nTop 20 most popular movies with over 200 ratings that user 399 has not seen:\n')
    # print_popular_for_user(399,20,200)

    # print('\nTop 20 users similar to user 399:')
    # [print('{:3d}: {:3d} | sim: {:.2f}'.format(i+1, m[0], m[1]))
    #   for i, m in enumerate(similar_users(399)[:20])]

    # print('\nTop 20 users similar to user 120:')
    # [print('{:3d}: {:3d} | sim: {:.2f}'.format(i+1, m[0], m[1]))
    #   for i, m in enumerate(similar_users(120)[:20])]
    #
    # print("\nUser 399's favorite movies:")
    # [print('{:' '>3}: {} stars {}'.format(i+1, m[1], all_movies[m[0]].title))
    #     for i, m in enumerate(sorted(all_users[399].get_movie_data(),
    #     key=lambda c: c[1], reverse=True)[:20])]
    #
    # print("\nUser 120's high-to-low movie ratings:")
    # [print('{:' '>3}: {} stars | {}'.format(*e)) for e in all_users[120].high_to_low()]


if __name__ == '__main__':
    main()
