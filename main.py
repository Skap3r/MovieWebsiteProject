import movie
import fresh_tomatoes

# Using Movie Class to create objects of my favorite movies.
interstellar = movie.Movie("Interstellar",
                           "How to not grow old",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_QL50_SY1000_CR0,0,640,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

the_martian = movie.Movie("The Martian",
                          "How to survive Mars",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

predestination = movie.Movie("Predestination",
                             "A man makes himself and on and on it goes",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAzODc3NjU1NzNeQTJeQWpwZ15BbWU4MDk5NTQ4NTMx._V1_QL50_SY1000_CR0,0,677,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=-FcK_UiVV40")

prometheus = movie.Movie("Prometheus",
                         "In search of our ancestors",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY3NzIyNTA2NV5BMl5BanBnXkFtZTcwNzE2NjI4Nw@@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=34cEo0VhfGE")

the_ring = movie.Movie("The Ring",
                       "Don't watch TV",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BNDA2NTg2NjE4Ml5BMl5BanBnXkFtZTYwMjYxMDg5._V1_QL50_.jpg",
                       "https://www.youtube.com/watch?v=_PkgRhzq_BQ")

dead_silence = movie.Movie("Dead Silence",
                           "Doll goes crazy", 
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyNDQwMTQ3OV5BMl5BanBnXkFtZTcwMTY5MzI0MQ@@._V1_QL50_.jpg",
                           "https://www.youtube.com/watch?v=8b_HVtHmK30")

the_exorcism_of_emily_rose = movie.Movie("The Exorcism of Emily Rose",
                           "A girl possessed by Satan gets exercised",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI2NTM5MjQ0Nl5BMl5BanBnXkFtZTcwNDAxNjAzMQ@@._V1_QL50_.jpg",
                           "https://www.youtube.com/watch?v=jsGIpxlgENY")

chappie = movie.Movie("Chappie",
                      "A military robot that learns too much",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNTI4NTIwNl5BMl5BanBnXkFtZTgwMjQ4MTI0NDE@._V1_QL50_SY1000_CR0,0,674,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=lyy7y0QOK-0")

inception = movie.Movie("Inception",
                        "A story about a dream stealer",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_QL50_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

the_matrix = movie.Movie("The Matrix",
                         "We are in a simulation!",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

# Adding movie objects to a list.
movies = [interstellar, the_martian, the_ring, prometheus, predestination, dead_silence,
           the_exorcism_of_emily_rose, the_matrix, chappie, inception]
fresh_tomatoes.open_movies_page(movies) # This method takes in a list of Movie objects and creates a webpage with all the movies in it.
