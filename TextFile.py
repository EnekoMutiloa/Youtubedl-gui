import os


class TextFile:

    def __init__(self):
        self.file = None
        self.name = None

    def create_text_file(self, name):
        self.name = name
        self.file = open(self.name, 'w')

    def close_and_delete_file(self):
        self.file.close()
        os.remove(self.name)

    def write_in_file(self, url):
        self.file.write(url)

    def get_name(self):
        return self.name
