import webbrowser

class Movie():
        """ This class takes in movie information and stores it in it's instance variables."""

	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		
        # opens the YouTube link provided and plays video
        def show_trailer(self):
                webbrowser.open(self.trailer_youtube)

                                
                
	 	
