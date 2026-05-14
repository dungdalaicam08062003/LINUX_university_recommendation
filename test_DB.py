import psycopg2

# Thông tin kết nối
conn = psycopg2.connect(
    dbname="university_db",
    user="dung",
    password="StrongPassword123!",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Thực hiện truy vấn
cur.execute("SELECT * FROM university;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Đóng kết nối
cur.close()
conn.close()
