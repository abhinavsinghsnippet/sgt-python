'''12. Movie Class with Rating
•	Create a class called Movie with attributes:
o	title: Title of the movie.
o	genre: Genre of the movie.
o	rating: IMDb rating of the movie.
•	Write methods to:
o	Display movie details.
o	Check if the movie rating is above 8 (considered “highly rated”).
•	Create instances of Movie and test these methods.
'''
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def display_details(self):
        print(f"Title: {self.title}, Genre: {self.genre}, IMDb Rating: {self.rating}")

    def is_highly_rated(self):
        return self.rating > 8


movie1 = Movie("Inception", "Science Fiction", 8.8)
movie2 = Movie("The Room", "Drama", 3.7)


movie1.display_details()
movie2.display_details()


print("Is 'Inception' highly rated?", movie1.is_highly_rated())
print("Is 'The Room' highly rated?", movie2.is_highly_rated())
