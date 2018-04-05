#=================================================================
# Python program: entertainment_center.py
# - Main Program entry point for movie_website project
#=================================================================

import fresh_tomatoes 
import media
import sys



if __name__ == "__main__":

    mode = "DHC_FAVORITES"   #TEACHER_FAVORITES or DHC_FAVORITES

     

    if mode == "TEACHER_FAVORITES":
        
        toy_story = media.Movie("Toy Story",
                                "A story of a boy and his toys that come to life",
                                "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                "https://www.youtube.com/watch?v=vwyZH85NQC4")
        
        avatar = media.Movie("Avatar",
                             "A marine on an alien planet",
                             "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                             "http://www.youtube.com/watch?v=-9ceBgWV8io")


        school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "http://www.youtube.com/watch?v=3PsUJFEBC74")


        ratatouille = media.Movie("Ratatouille",
                             "A rat is a chef in Paris",
                             "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                             "http://www.youtube.com/watch?v=c3sBBRxDAqk")

        midnight_in_paris = media.Movie("Midnight in Paris",
                             "Going back in time to meet authors",
                             "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                             "http://www.youtube.com/watch?v=atLg2wQQxvU")

        hunger_games = media.Movie("Hunger Games",
                             "A really real reality show",
                             "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                             "http://www.youtube.com/watch?v=PbA63a7H0bo")

        # Create list of movie objects
        movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
        

    elif mode == "DHC_FAVORITES":
     
        #----------------------------------------------------------
        # Independence Day
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Independence_day_movieposter.jpg/220px-Independence_day_movieposter.jpg
        # - Trailer: https://www.youtube.com/watch?v=NZZvtQtdbzM
        #   - Alternate: https://www.youtube.com/watch?v=B1E7h3SeMDk
        independence_day = media.Movie("Independence Day",
                                       "The question of whether or not we are alone in the universe has been answered",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Independence_day_movieposter.jpg/220px-Independence_day_movieposter.jpg",
                                       "https://www.youtube.com/watch?v=NZZvtQtdbzM")

        #----------------------------------------------------------
        # Alien:
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Alien_movie_poster.jpg/220px-Alien_movie_poster.jpg
        # - Trailer: https://www.youtube.com/watch?v=LjLamj-b0I8

        alien = media.Movie("Alien",
                                       "In space no one can hear you scream",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Alien_movie_poster.jpg/220px-Alien_movie_poster.jpg",
                                       "https://www.youtube.com/watch?v=LjLamj-b0I8")

        #----------------------------------------------------------
        # Super Troopers
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg
        # - Trailer: https://www.youtube.com/watch?v=2-9D2qUHN-E

        super_troopers = media.Movie("Super Troopers",
                                       "Altered State Police",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg",
                                       "https://www.youtube.com/watch?v=2-9D2qUHN-E")
       

        #----------------------------------------------------------
        # True Lies
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/8/81/True_Lies_poster.png/220px-True_Lies_poster.png 
        # - Trailer: https://www.youtube.com/watch?v=3B7HG8_xbDw

        true_lies = media.Movie("True Lies",
                                       "When he said I do, he never said what he did",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/True_Lies_poster.png/220px-True_Lies_poster.png",
                                       "https://www.youtube.com/watch?v=3B7HG8_xbDw")


        #----------------------------------------------------------
        # I, Robot
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Movie_poster_i_robot.jpg/220px-Movie_poster_i_robot.jpg
        # - Trailer: https://www.youtube.com/watch?v=rL6RRIOZyCM

        i_robot = media.Movie("I, Robot",
                                       "No man saw it coming",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Movie_poster_i_robot.jpg/220px-Movie_poster_i_robot.jpg",
                                       "https://www.youtube.com/watch?v=rL6RRIOZyCM")


        #----------------------------------------------------------
        # Stargate
        # Poster: https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Stargateposter.jpg/220px-Stargateposter.jpg
        # Trailer: https://www.youtube.com/watch?v=kiJtZUPvJxY

        stargate = media.Movie("Stargate",
                                       "It will take you a million light years from home ... but will it bring you back?",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Stargateposter.jpg/220px-Stargateposter.jpg",
                                       "https://www.youtube.com/watch?v=kiJtZUPvJxY")


        #----------------------------------------------------------
        # Blazing Saddles
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Blazing_saddles_movie_poster.jpg/225px-Blazing_saddles_movie_poster.jpg
        # - Trailer: https://www.youtube.com/watch?v=VKayG1TrfuE

        blazing_saddles = media.Movie("Blazing Saddles",
                                       "or never give a saga an even break",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Blazing_saddles_movie_poster.jpg/225px-Blazing_saddles_movie_poster.jpg",
                                       "https://www.youtube.com/watch?v=VKayG1TrfuE")


        #----------------------------------------------------------
        # Predators
        # - Poster: https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Predators_54632_glg.jpg/220px-Predators_54632_glg.jpg 
        # - Trailer: https://www.youtube.com/watch?v=igKKWJw88Kk

        predators = media.Movie("Predators",
                                       "They are the most dangerous killers on the planet. But this is not our planet ...",
                                       "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Predators_54632_glg.jpg/220px-Predators_54632_glg.jpg",
                                       "https://www.youtube.com/watch?v=igKKWJw88Kk")


        #----------------------------------------------------------
        # GhostBusters
        # - Poster: https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png 
        # - Trailer: https://www.youtube.com/watch?v=vntAEVjPBzQ

        ghostbusters = media.Movie("Ghostbusters",
                                       "Who ya gonna call?",
                                       "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png",
                                       "https://www.youtube.com/watch?v=vntAEVjPBzQ")




        # Create list of movie objects
        movies = [independence_day, alien, super_troopers, true_lies, i_robot, stargate, blazing_saddles, predators, ghostbusters]

    else:
        print("Unknown mode: "+mode+" Program Error Exit.")
        sys.exit(99)  

    # Generate and Open Web page to play movie trailers
    fresh_tomatoes.open_movies_page(movies) 

   
    sys.exit(0)