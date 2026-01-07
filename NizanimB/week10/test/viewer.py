class Viewer:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.listOfViewed = []
        self.listOfRated = []

    def watch_content(self, content):
        if not content in self.listOfViewed:
            self.listOfViewed.append(content)
            content.add_view()
            return True
        return False

    def rate_content(self, content, rating):
        if content in self.listOfRated:
            return False
        content.add_rating(rating)
        self.listOfRated.append(content)
        return True


    def print_details(self):

        print(f"Name: {self.user_name}")
        print("Content Watched:")

        for content in self.listOfViewed:
            print(f" - {content.content_name}")

        print("Content Rated:")

        for content in self.listOfRated:
            print(f" - {content.content_name} Rating: {content.get_average_rating()}")