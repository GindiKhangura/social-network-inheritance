from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if not timestamp:
            timestamp = datetime.now()
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

    def get_formatted_timestamp(self):
        return self.timestamp.strftime('%A, %b %d, %Y')

    def __repr__(self):
        return '{classname}: {text}'.format(classname=self.__class__.__name__, text=self.text)


class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{firstname} {lastname}: "{text}"\n\t{timestamp}'.format(firstname=self.user.first_name, lastname=self.user.last_name, text=self.text, timestamp=self.get_formatted_timestamp())


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{firstname} {lastname}: "{text}"\n\t{image_url}\n\t{timestamp}'.format(firstname=self.user.first_name, lastname=self.user.last_name, text=self.text, image_url=self.image_url, timestamp=self.get_formatted_timestamp())


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{firstname} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(firstname=self.user.first_name, lastname=self.user.last_name, text=self.text, latitude=self.latitude, longitude=self.longitude, timestamp=self.get_formatted_timestamp())
