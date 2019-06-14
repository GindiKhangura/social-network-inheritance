

class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        timeline = []
        for following in self.following:
            timeline.extend(following.posts)
        return timeline

    def follow(self, other):
        self.following.append(other)

    def __repr__(self):
        return '{classname}: "{firstname} {lastname}"'.format(classname=self.__class__.__name__, firstname=self.first_name, lastname=self.last_name)
