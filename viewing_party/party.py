# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {"title": title, "genre": genre, "rating": rating}
    return movie

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    user_watchlist = user_data["watchlist"]
    user_watched = user_data["watched"]
    #print(type(user_watchlist))
    watching_index = None
    for index in range(len(user_watchlist)):
        #print(index)
        movie = user_watchlist[index]
        if movie["title"] == movie_title:
            watching_index = index
    if watching_index is not None:
        user_watched.append(user_watchlist[watching_index])
        user_watchlist.pop(watching_index)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    rating_sum = 0
    number_of_ratings = len(watched_list)
    if number_of_ratings == 0:
        return 0

    for movie in watched_list:
        rating_sum += movie["rating"]

    return rating_sum/number_of_ratings

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if not watched_list:
        return None
    genre_counter = {}
    for movie in watched_list:
        genre = movie["genre"]
        if genre in genre_counter.keys():
            genre_counter[genre] += 1
        else:
            genre_counter[genre] = 1
    
    most_watched_count = max(genre_counter.values())
    for counted_genre in genre_counter.keys():
        if genre_counter[counted_genre] == most_watched_count:
            return counted_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# ----------------------------------------- 
def get_unique_watched(user_data):
    friends = user_data["friends"]
    user_movie_list = user_data["watched"]
    unique_movie_names = set()
    for movie in user_movie_list:
        unique_movie_names.add(movie["title"])
    
    for friend in friends:
        friend_watched_list = friend["watched"]
        for movie in friend_watched_list:
            if movie["title"] in unique_movie_names:
                unique_movie_names.remove(movie["title"])
    
    unique_movies = []
    for movie in user_movie_list:
        if movie["title"] in unique_movie_names:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends = user_data["friends"]
    user_movie_list = user_data["watched"]
    
    user_movie_names = set()
    for movie in user_movie_list:
        user_movie_names.add(movie["title"])

    only_friends_watched_list = []
    friends_movie_names = set()
    for friend in friends:
        friend_watched_list = friend["watched"]
        for movie in friend_watched_list:
            if (movie["title"] not in user_movie_names and 
                movie["title"] not in friends_movie_names):
                friends_movie_names.add(movie["title"])
                only_friends_watched_list.append(movie)
    
    return only_friends_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    possible_recs = get_friends_unique_watched(user_data)
    available_recs = []
    for rec in possible_recs:
        if rec["host"] in user_data["subscriptions"]:
            available_recs.append(rec)
    
    return available_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    possible_recs = get_friends_unique_watched(user_data)
    most_frequent_genre = get_most_watched_genre(user_data)
    genre_recs = []
    for rec in possible_recs:
        if rec["genre"] == most_frequent_genre:
            genre_recs.append(rec)
    
    return genre_recs

def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    user_favorite_names = set()
    for favorite in user_favorites:
        user_favorite_names.add(favorite["title"])

    movie_recs = []
    friends_havent_watched = get_unique_watched(user_data)
    for movie in friends_havent_watched:
        if movie["title"] in user_favorite_names:
            movie_recs.append(movie)

    return movie_recs