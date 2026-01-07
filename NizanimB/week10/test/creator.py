from viewer import Viewer

class Creator(Viewer):

    def __init__(self, user_id, user_name):
        super().__init__(user_id, user_name)
        self.listOfUploads = []

    def upload_content(self, content):
        if len(self.listOfUploads) > 10 or content in self.listOfUploads:
            return False
        self.listOfUploads.append(content)
        return True

    def print_details(self):

        print(f"Name: {self.user_name}")
        print("Content Uploaded:")

        for content in self.listOfUploads:
            print(f" - {content.content_name}")