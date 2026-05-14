class field_of_study:
    def __init__(self, code_field_of_study, ID_university, fee_university, info_url, description):
        self.code_field_of_study = code_field_of_study
        self.ID_university = ID_university
        self.fee_university = fee_university
        self.info_url = info_url
        self.description = description

    def get_info(self):
        return f"Field of Study: {self.code_field_of_study}, University ID: {self.ID_university}, Fee: {self.fee_university}, Info URL: {self.info_url}, Description: {self.description}"

    def to_dict(self):
        return {
            'code_field_of_study': self.code_field_of_study,
            'ID_university': self.ID_university,
            'fee_university': self.fee_university,
            'info_url': self.info_url,
            'description': self.description
        }