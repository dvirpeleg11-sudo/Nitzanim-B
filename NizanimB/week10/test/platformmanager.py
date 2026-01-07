from creator import Creator

class PlatformManager(Creator):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.listOfCreators = []

    def add_creator(self, creator):
        if creator in self.listOfCreators:
            return False
        self.listOfCreators.append(creator)
        return True

    def find_most_successful_creator(self):


        most_views = self.listOfCreators[0].listOfUploads[0].number_of_views
        result = ["name", "content name", most_views]

        for creator in self.listOfCreators:
            for content in creator.listOfUploads:
                current_content_views = content.number_of_views
                if current_content_views >= most_views:
                    result[0] = creator.user_name
                    result[1] = content.content_name
                    result[2] = current_content_views

        return tuple(result)

    def print_details(self):

        print(f"Name: {self.user_name}")
        print("Creators Under Manager:")

        for creator in self.listOfCreators:
            print(f" - {creator.user_name}")