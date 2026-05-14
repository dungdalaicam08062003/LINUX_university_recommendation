import routes.university as u1

if __name__ == "__main__":
    university_info = u1.get_university_info()
    print(university_info)

    university_id = 1
    industry_info_list = u1.get_list_industry_info_university(university_id)
    print(industry_info_list)