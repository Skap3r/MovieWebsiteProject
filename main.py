import movie
import fresh_tomatoes

# Using Movie Class to create objects of my favorite movies.
interstellar = movie.Movie("Interstellar",
                           "How to not grow old",
                           "http://bit.ly/2uqGWDn",
                           "https://youtu.be/zSWdZVtXT7E")

the_martian = movie.Movie("The Martian",
                          "How to survive Mars",
                          "http://bit.ly/2wvxJ9T",
                          "https://youtu.be/ej3ioOneTy8")

predestination = movie.Movie("Predestination",
                             "A man makes himself and on and on it goes",
                             "http://bit.ly/2vQfSNi",
                             "https://youtu.be/F_CCjXQ9aYw")

prometheus = movie.Movie("Prometheus",
                         "In search of our ancestors",
                         "http://bit.ly/2vQOsHN",
                         "https://youtu.be/34cEo0VhfGE")

the_ring = movie.Movie("The Ring",
                       "Don't watch TV",
                       "http://bit.ly/2hOzFHm",
                       "https://youtu.be/_PkgRhzq_BQ")

dead_silence = movie.Movie("Dead Silence",
                           "Doll goes crazy",
                           "http://bit.ly/2vmJsJH",
                           "https://youtu.be/8b_HVtHmK30")

exorcism_of_emily_rose = movie.Movie("The Exorcism of Emily Rose",
                                     "A possessed girl gets excercised",
                                     "http://bit.ly/2vIL2pV",
                                     "https://youtu.be/jsGIpxlgENY")

chappie = movie.Movie("Chappie",
                      "A military robot that learns too much",
                      "http://bit.ly/2wLIQLk",
                      "https://youtu.be/lyy7y0QOK-0")

inception = movie.Movie("Inception",
                        "A story about a dream stealer",
                        "http://bit.ly/2vSPJOq",
                        "https://youtu.be/YoHD9XEInc0")

the_matrix = movie.Movie("The Matrix",
                         "We are in a simulation!",
                         "http://bit.ly/2wLFnw7",
                         "https://youtu.be/m8e-FF8MsqU")

# Adding movie objects to a list.
movies = [interstellar, the_martian, the_ring, prometheus, predestination,
          dead_silence, exorcism_of_emily_rose, the_matrix, chappie, inception]
# The following method takes in a list of Movie objects and creates a
# webpage with all the movies in it.
fresh_tomatoes.open_movies_page(movies)
