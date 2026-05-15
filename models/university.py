class university:
    def __init__(self, id, name, location, url):
        self.id = id
        self.name = name
        self.location = location
        self.url = url

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "url": self.url
        }
