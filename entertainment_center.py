#!/usr/bin/env python
# =================================================================
# Python program: entertainment_center.py
# - Main Program entry point for movie_website project
# =================================================================

import fresh_tomatoes
import media
import sys


if __name__ == "__main__":

    # -------------------------------------
    # Create instances of the Movie object
    # -------------------------------------
    synopsis_lookup = {}

    synopsis_lookup["independence_day"] = (
        "Synopsis: \n"
        "Independence Day is a 1996 American science fiction action film"
        "directed and co-written by Roland Emmerich."
        "The film focuses on disparate groups of people who converge"
        "in the Nevada desert in the aftermath of a worldwide attack"
        "by an extraterrestrial race of unknown origin.\n"
        "With the other people of the world, they launch a last-ditch"
        "counterattack on July 4 - Independence Day in the United States.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    independence_day = media.Movie("Independence Day",
                                   synopsis_lookup["independence_day"],
                                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/bb/Independence_day_movieposter.jpg/220px-Independence_day_movieposter.jpg",  # NOQA
                                   "https://www.youtube.com/watch?v=NZZvtQtdbzM")  # NOQA

    synopsis_lookup["alien"] = (
        "Synopsis:\n"
        "Alien is a 1979 science fiction horror film directed by "
        "Ridley Scott, and starring Sigourney Weaver, Tom Skerritt, "
        "Veronica Cartwright, Harry Dean Stanton, John Hurt, Ian Holm "
        "and Yaphet Kotto.\n"
        "It is the first movie in what became a large Alien franchise.\n"
        "The film's title refers to a highly aggressive extraterrestrial "
        "creature that stalks and attacks the crew of a spaceship.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    alien = media.Movie("Alien",
                        synopsis_lookup["alien"],
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Alien_movie_poster.jpg/220px-Alien_movie_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=LjLamj-b0I8")  # NOQA

    synopsis_lookup["super_troopers"] = (
        "Synopsis:\n"
        "Super Troopers is a 2001 American crime-comedy film directed "
        "by Jay Chandrasekhar, written by and starring the Broken Lizard "
        "comedy group (Jay Chandrasekhar, Kevin Heffernan, Steve Lemme, "
        "Paul Soter and Erik Stolhanske).\n"
        "The film takes place in the fictional town of Spurbury, Vermont, "
        "near the Canada-US border. The plot centers on five Vermont state "
        "troopers who seem to have more of a knack for pranks than "
        "police work."
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    super_troopers = media.Movie("Super Troopers",
                                 synopsis_lookup["super_troopers"],
                                 "https://upload.wikimedia.org/wikipedia/en/thumb/1/19/Supertrooper.jpg/220px-Supertrooper.jpg",  # NOQA
                                 "https://www.youtube.com/watch?v=2-9D2qUHN-E")  # NOQA

    synopsis_lookup["true_lies"] = (
        "Synopsis:\n"
        "True Lies is a 1994 American action film written, directed "
        "and co-produced by James Cameron."
        "It stars Arnold Schwarzenegger, Jamie Lee Curtis, Tom Arnold, "
        "Art Malik, Tia Carrere, Bill Paxton, Eliza Dushku, "
        "Grant Heslov and Charlton Heston.\n"
        "It is a remake of the 1991 French comedy film La Totale!\n"
        "The film follows U.S. government agent Harry Tasker "
        "(Schwarzenegger), who balances his life as a spy with his "
        "familial duties.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    true_lies = media.Movie("True Lies",
                            synopsis_lookup["true_lies"],
                            "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/True_Lies_poster.png/220px-True_Lies_poster.png",  # NOQA
                            "https://www.youtube.com/watch?v=3B7HG8_xbDw")  # NOQA

    synopsis_lookup["i_robot"] = (
        "Synopsis:\n"
        "I, Robot (stylized as i,robot) is a 2004 American science fiction "
        "action film directed by Alex Proyas."
        "The film stars Will Smith, Bridget Moynahan, Bruce Greenwood, "
        "James Cromwell, Chi McBride and Alan Tudyk.\n"
        "In the year 2035, humanoid robots serve humanity, which is "
        "protected by the Three Laws of Robotics. Del Spooner, a Chicago "
        "police detective, hates and distrusts robots because he was "
        "rescued from a car crash by a robot using cold logic (his survival "
        "was statistically more likely), leaving a 12-year-old girl to "
        "drown. Spooner's critical injuries were repaired with a "
        "cybernetic left arm, lung, and ribs, personally implanted by the "
        "co-founder of U.S. Robots and Mechanical Men (USR), Dr. Alfred "
        "Lanning.\n"
        "When Lanning falls to his death from his office window, "
        "the CEO of USR Lawrence Robertson and the police declare it a "
        "suicide, but Spooner is skeptical.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    i_robot = media.Movie("I, Robot",
                          synopsis_lookup["i_robot"],
                          "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Movie_poster_i_robot.jpg/220px-Movie_poster_i_robot.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=rL6RRIOZyCM")  # NOQA

    synopsis_lookup["stargate"] = (
        "Synopsis:\n"
        "Stargate is a 1994 science fiction adventure film released "
        "through Metro-Goldwyn-Mayer (MGM) and Carolco Pictures. "
        "Written by Dean Devlin and Roland Emmerich, "
        "the film is the first release in the Stargate franchise. "
        "Directed by Emmerich, the film stars Kurt Russell, James Spader, "
        "Jaye Davidson, Alexis Cruz, Mili Avital, and Viveca Lindfors.\n"
        "The plot centers on the premise of a \"Stargate\", an ancient "
        "ring-shaped device that creates a wormhole enabling travel to a "
        "similar device elsewhere in the universe. The film's central "
        "plot explores the theory of extraterrestrial beings having an "
        "influence upon human civilization.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    stargate = media.Movie("Stargate",
                           synopsis_lookup["stargate"],
                           "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Stargateposter.jpg/220px-Stargateposter.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=kiJtZUPvJxY")  # NOQA

    synopsis_lookup["blazing_saddles"] = (
        "Synopsis:\n"
        "Blazing Saddles is a 1974 American satirical Western comedy "
        "film directed by Mel Brooks. "
        "Starring Cleavon Little and Gene Wilder, the film was written by "
        "Brooks, Andrew Bergman, Richard Pryor, Norman Steinberg, and "
        "and Al Uger, and was based on Bergman's story and draft.\n"
        "The film received generally positive reviews from critics "
        "and audiences, was nominated for three Academy Awards, and is "
        "ranked No. 6 on the American Film Institute's "
        "100 Years...100 Laughs list.\n"
        "The film satirizes the racism obscured by myth-making "
        "Hollywood accounts of the American West, "
        "with the hero being a black sheriff in an all-white town. "
        "The film is full of deliberate anachronisms, from the Count Basie "
        "Orchestra playing \"April in Paris\" in the Wild West, to "
        "Slim Pickens referring to the Wide World of Sports, "
        "to the German army of World War II.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    blazing_saddles = media.Movie("Blazing Saddles",
                                  synopsis_lookup["blazing_saddles"],
                                  "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Blazing_saddles_movie_poster.jpg/225px-Blazing_saddles_movie_poster.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=VKayG1TrfuE")  # NOQA

    synopsis_lookup["predators"] = (
        "Synopsis:\n"
        "Predators is a 2010 American science-fiction action film "
        "directed by Nimrod Antal and starring Adrien Brody, Topher Grace, "
        "Alice Braga, Walton Goggins, Laurence Fishburne, Danny Trejo, "
        "Mahershala Ali, Oleg Taktarov, and Louis Ozawa Changchien. "
        "It was distributed by 20th Century Fox. It is the third "
        "installment of the Predator franchise, following Predator (1987) "
        "and Predator 2 (1990). Another film, The Predator, "
        "is set for 2018.\n"
        "The film follows an ensemble cast of characters including "
        "Royce (Adrien Brody), a mercenary who appears in an unidentified "
        "jungle among other murderers and otherwise undesirable people. "
        "They find that they have been abducted and placed on a planet "
        "which acts as a game reserve for two warring tribes of "
        "extraterrestrial killers, and actively look for a way to ."
        "return to Earth.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    predators = media.Movie("Predators",
                            synopsis_lookup["predators"],
                            "https://upload.wikimedia.org/wikipedia/en/thumb/1/12/Predators_54632_glg.jpg/220px-Predators_54632_glg.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=igKKWJw88Kk")  # NOQA

    synopsis_lookup["ghostbusters"] = (
        "Synopsis:\n"
        "Ghostbusters is a 1984 American comedy film directed and produced "
        "by Ivan Reitman and written by Dan Aykroyd and Harold Ramis. "
        "It stars Bill Murray, Aykroyd and Ramis as eccentric "
        "parapsychologists who start a ghost-catching business in "
        "New York City. Sigourney Weaver and Rick Moranis co-star as a "
        "client and her neighbor, and Ernie Hudson as the Ghostbusters' "
        "first recruit. \n"
        "Parapsychologists Peter Venkman, Raymond Stantz, and Egon Spengler "
        "are scientists working for Columbia University. After being "
        "called to the New York Public Library to investigate recent "
        "paranormal activity, they encounter a full-fledged ghost but "
        "she frightens them away. They lose their jobs, so the trio "
        "establish the Ghostbusters, a paranormal investigation and "
        "elimination service.\n"
        "\n"
        "-----------------------------\n"
        "Click to see Movie Trailer\n"
        "-----------------------------\n")
    ghostbusters = media.Movie("Ghostbusters",
                               synopsis_lookup["ghostbusters"],
                               "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png",  # NOQA
                               "https://www.youtube.com/watch?v=vntAEVjPBzQ")  # NOQA

    # Create list of movie objects
    movies = [independence_day, alien, super_troopers, true_lies, i_robot,
              stargate, blazing_saddles, predators, ghostbusters]

    # Generate and Open Web page to play movie trailers
    fresh_tomatoes.open_movies_page(movies)

    sys.exit(0)
