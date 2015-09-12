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
        '''Returns dictionary of users and their ratings of this Movie'''
        ret = [r for _, r in self.user_ratings.items()]
        print(ret)
        return ret

    def ave_user_rating(self):
        u_r = self.get_user_ratings()
        return sum(u_r)/len(u_r)

    def get_user_ratings_w_movie_id(self):
        return self.user_ratings.values()


class User:
    def __init__(self, id):
        self.id = int(id)
        self.movie_ratings = {}
        # if 'age' in kwargs:
        #     self.age = kwargs['age']
        # self.movie_stars = {}
        all_users[self.id] = self

    def __str__(self):
        return 'User(id={})'.format(self.id)

    def __repr__(self):
        return self.__str__()

    def add_movie_rating(self, rating):
        self.movie_ratings[rating.movie_id] = rating.stars

    def get_movie_ratings(self):
        '''Returns list of all star ratings for this Movie'''
        return [r for _, r in self.movie_ratings.items()]

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


def popular_movies(num_results):
    return sorted([all_movies[m_id].ave_user_rating() for m_id, _ in all_movies], reverse=True)[:num_results]


def main():

    init_structures()

    print(popular_movies)





if __name__ == '__main__':
    main()
