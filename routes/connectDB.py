import psycopg2

# Thông tin kết nối
conn = psycopg2.connect(
    dbname="university_db",
    user="dung",
    password="matkhau_manh",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
def open_connection():
    try:
        conn = psycopg2.connect(
            dbname="university_db",
            user="dung",
            password="matkhau_manh",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None
# Thực hiện truy vấn
cur.execute("SELECT * FROM university;")
rows = cur.fetchall()

for row in rows:
    print(row)

# Đóng kết nối
cur.close()
conn.close()
