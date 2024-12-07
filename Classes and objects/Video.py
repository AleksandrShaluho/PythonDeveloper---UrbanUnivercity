class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title

    def __contains__(self, item):
        if item.lower() in self.title.lower():
            return True
        else:
            return False

    def __eq__(self, other):
        if isinstance(other, Video):
            if self.title == other.title:
                return True
            else:
                return False
        else:
            return 'Нужно сравнивать два объекта класса Video'

    def __hash__(self):
        return hash(self.title)
