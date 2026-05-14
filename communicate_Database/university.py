import models.university as university
import models.university_data as university_data
import communicate_Database.connectDB as db
def get_university_info():
    # Tạo đối tượng university_data
    conn = db.open_connection()
    if not conn:
        return {"error": "Failed to connect to database"}

    sql = "SELECT * FROM university;"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if rows:
            university_info = university.university(
                name=rows[0][0],
                location=rows[0][1],
                url=rows[0][2]
            )
            return university_info.to_dict()
        else:
            return {"error": "University not found"}
    except Exception as e:
        print(f"Error fetching university info: {e}")
        return {"error": "Failed to fetch university info"}
    finally:
        if conn:
            conn.close()
def get_list_industry_info_university(university_id):
    conn = db.open_connection()
    if not conn:
        return {"error": "Failed to connect to database"}

    sql = "SELECT * from university_data where ID_university = %s"
    try:
        cur = conn.cursor()
        cur.execute(sql, (university_id,))
        rows = cur.fetchall()
        if rows:
            industry_info_list = []
            for row in rows:
                industry_info = university_data.industry_data(
                    ID_industry=row[0],
                    name_industry=row[1],
                    description_industry=row[2]
                )
                industry_info_list.append(industry_info.to_dict())
            return industry_info_list
        else:
            return {"error": "No industry information found for the specified university"}
    except Exception as e:
        print(f"Error fetching industry information: {e}")
        return {"error": "Failed to fetch industry information"}
    finally:
        if conn:
            conn.close()