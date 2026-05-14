class university:
    def __init__(self, name, location, url):
        self.name = name
        self.location = location
        self.url = url

    def get_info(self):
        return f"{self.name} is located in {self.location} and can be visited at {self.url}."
    def to_dict(self):
        return {
            'name': self.name,
            'location': self.location,
            'url': self.url
        }
