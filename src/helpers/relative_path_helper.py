import os


class RelativePathHelper(object):
    @staticmethod
    def return_path(relative_path):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, relative_path)
