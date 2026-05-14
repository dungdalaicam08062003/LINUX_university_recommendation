-- psql -U dung -h localhost -d university_db
-- matkhau_manh
CREATE TABLE university (
  ID_university SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  location_ID VARCHAR(50),
  url VARCHAR(255)
);

CREATE TABLE field_of_study (
  ID_field_of_study SERIAL PRIMARY KEY,
  code_field_of_study VARCHAR(50) NOT NULL,
  ID_university INT REFERENCES university(ID_university) ON DELETE CASCADE,
  fee_university NUMERIC,
  info_url VARCHAR(512),
  description TEXT
);


CREATE TABLE university_data (
  ID SERIAL PRIMARY KEY,
  ID_university INT REFERENCES university(ID_university) ON DELETE CASCADE,
  new_data_description TEXT,
  url VARCHAR(255)
);

CREATE TABLE users (
  ID SERIAL PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

INSERT INTO university (name, location_ID, url)
VALUES 
('Đại học A', 'DN', 'https://uni-a.edu.vn'),
('Đại học B', 'HN', 'https://uni-b.edu.vn');

INSERT INTO field_of_study (code_field_of_study, ID_university, fee_university, info_url, description)
VALUES 
('CNTT', 1, 15000000, 'https://uni-a.edu.vn/cntt', 'Ngành CNTT tại Đại học A'),
('Kinh tế', 1, 12000000, 'https://uni-a.edu.vn/kinhte', 'Ngành Kinh tế tại Đại học A'),
('CNTT', 2, 14000000, 'https://uni-b.edu.vn/cntt', 'Ngành CNTT tại Đại học B'),
('Kinh tế', 2, 11000000, 'https://uni-b.edu.vn/kinhte', 'Ngành Kinh tế tại Đại học B');