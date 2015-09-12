import csv

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
        '''Returns list of each movie_id in user's movie_ratings dict'''
        return [i for i, m in self.movie_ratings.items()]

    def ave_movie_rating(self):
        m_r = self.get_movie_ratings()
        return sum(m_r)/len(m_r)

    def get_movie_ratings_w_user_id(self):
        return self.movie_ratings.values()


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


def main():
    print('Initializing data structures from MovieLens data files . . .')
    init_structures()
    print('Initialization complete.\n')

    # There are 141 movies with just 1 user rating.

    # print(pop_movies(20, 200))
    print('Top 30 most popular movies with over 200 ratings:')
    [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(pop_movies(30,200))]

    print('\nTop 20 most popular movies with over 200 ratings that user 399 has not seen:')
    # print(pop_movies_for_user(399, 20, 200))
    [print('{:' '>3}: {}'.format(i+1, m)) for i, m in enumerate(pop_movies_for_user(399,20,200))]


if __name__ == '__main__':
    main()
