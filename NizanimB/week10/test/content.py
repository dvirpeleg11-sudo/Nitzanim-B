class Content:

    def __init__(self, content_name, contentCreator, genre):
        self.content_name = content_name
        self.contentCreator = contentCreator
        self.genre = genre
        self.number_of_views = 0
        self.listOfRatings = []

    def add_view(self):
        self.number_of_views += 1

    def add_rating(self, rating):
        if 0 <= rating and rating <= 5:
            self.listOfRatings.append(rating)
            return True

        print("rating is not between 0 - 5.")
        return False

    def get_average_rating(self):
        ratings_sum = 0
        number_of_ratings = len(self.listOfRatings)

        for rating in self.listOfRatings:
            ratings_sum += rating

        return ratings_sum / number_of_ratings

    def set_genre(self, genre):
        if genre == "Action" or genre == "Comedy" or genre == "Drama" or genre == "Science":
            self.genre = genre
            return True

        print("there is not such a genre.")
        return False

    def print_details(self):
        print(f"Content Name: {self.content_name}")
        print(f"Genre: {self.genre}")
        print(f"Number of Views: {self.number_of_views}")