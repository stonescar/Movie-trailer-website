import webbrowser


class Movie():
    """Movie()
    Stores information about movies.

    Stores title, storyline, IMDB rating and urls to poster art, trailer and
    IMDB page. Compatible with fresh_tomatoes to generate a trailer web site.
    1: Import media and fresh_tomatoes
    2: Create objects of the movies you want to display
    3: Call fresh_tomatoes.open_movies_page(movies) with the movies as a list
       as an argument

    Attributes:
        title:                  The movie's title
        storyline:              Short summary of the story
        poster_image_url:       URL to the movie's poster art
        trailer_youtube_url:    Full link to the movie's trailer on youtube
        imdb_url:               Full link to the movie's IMDB page
        imdb_rating:            The movie's IMDB rating (given as a float)

    Methods:
        show(target):           Show the movie's IMDB page('imdb' (default)),
                                trailer('trailer') or poster('poster')
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url,
                 imdb_url, imdb_rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url
        self.imdb_rating = imdb_rating

    def show(self, target):
        """Movie.show(target)
    Shows the movie's IMDB page, trailer or poster. Takes one argument.
    Enter one of the following as the target:
        imdb:       Open the movie's IMDB page (default)
        trailer:    Play the movie's trailer
        poster:     Show the movie's poster
        """
        if target == 'trailer':
            webbrowser.open(self.trailer_youtube_url)
        elif target == 'poster':
            webbrowser.open(self.poster_image_url)
        else:
            webbrowser.open(self.imdb_url)
