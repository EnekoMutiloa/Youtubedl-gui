import os


class TextFile:

    def __init__(self):
        self.file = None

    def create_text_file(self):
        self.file = open('list.txt', 'w')

    def close_and_delete_file(self):
        self.file.close()
        os.remove(self.file)

    def write_in_file(self, url):
        self.file.write(url)

