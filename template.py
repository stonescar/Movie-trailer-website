import media
import fresh_tomatoes

# Make your own instances of your favorite movies like so:
# movie = media.Movie(title,
#                     storyline,
#                     poster_image_url,
#                     youtube_trailer_url,
#                     imdb_url,
#                     imdb_rating)
#
# Example:
# dark_knight = media.Movie("The Dark Knight",
#                           """When the menace known as the Joker wreaks havoc
#                           and chaos on the people of Gotham, the Dark Knight
#                           must come to terms with one of the greatest
#                           psychological tests of his ability to fight
#                           injustice.""",
#                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg", # NOQA
#                           "https://www.youtube.com/watch?v=EXeTwQWrcwY",
#                           "http://www.imdb.com/title/tt0468569/",
#                           9.0)
#
# Create as many instances as you want
# MAKE SURE TO INCLUDE THE INSTANCES IN THE LIST 'movies' ON LINE 27!

movies = []
fresh_tomatoes.open_movies_page(movies)
