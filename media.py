# =================================================================
# Python program: media.py
# - Classes for movie_website project
# =================================================================

import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Constructor initializes data from args.

           Args:
           - Param1: Movie Title String
           - Param2: Movie Synopsis Storyline string
                     - Feeds poster img title attr (hover tooltip popup)
           - Param3: URL string for Movie Poster Image
           - Param4: URL string for YouTube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
