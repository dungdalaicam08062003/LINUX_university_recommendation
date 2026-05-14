class university_data:
    def __init__(self, ID_university, new_data_description, url_info):
        self.ID_university = ID_university
        self.new_data_description = new_data_description
        self.url_info = url_info
    def get_info(self):
        return f"University_data: {self.ID_university}, Description: {self.new_data_description}, More info: {self.url_info}"
    def to_dict(self):
        return {
            'ID_university': self.ID_university,
            'new_data_description': self.new_data_description,
            'url_info': self.url_info
        }