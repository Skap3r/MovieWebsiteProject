# Description

A webpage that displays a list of movies and it's trailer.

# Installation

To download the project files click [here](https://drive.google.com/file/d/0Bx-eO8wDMop7YnhPdzQ0akM2TFU/view?usp=sharing) and extract it.

You need Python 2.7 or higher installed to add movies of your own and compile the program. To download Python click [here](https://www.python.org/downloads/).

After installing Python:
- Open the command line on Mac and type: `python main.py` (works in Windows command prompt too)
- On Windows (using Git Bash) type: `winpty python main.py`

# Usage

Run the `fresh_tomatoes.html` file. Click on the movie poster to play trailer.  
To add movies of your own, edit the `main.py` file and create Movie class objects. Then add it to the list `movies`. 
Example code:
```
movie_name = movie.Movie("movie_title",
                         "movie_description",
                         "poster_image_link",
                         "youtube_trailer_link")
```
