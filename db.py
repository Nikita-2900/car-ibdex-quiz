import sqlite3
con = sqlite3.connect("car.db")
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS cars (
    car_id INTEGER,
    car_name TEXT,
    image TEXT)''')
cur.execute("""INSERT INTO cars VALUES
    (1, "ВАЗ-2101", "image1.jpg"),
    (2, "ВАЗ-2102", "image2.jpg"),
    (3, "ВАЗ-2103", "image3.jpg"),
    (4, "ВАЗ-2104", "image4.jpg"),
    (5, "ВАЗ-2105", "image5.jpg"),
    (6, "ВАЗ-2106", "image6.jpg"),
    (7, "ВАЗ-2107", "image7.jpg"),
    (8, "ВАЗ-2108", "image8.jpg"),
    (9, "ВАЗ-2109", "image9.jpg"),
    (10, "ВАЗ-2110", "image10.jpg"),
    (11, "ВАЗ-2111", "image11.jpg"),
    (12, "ВАЗ-2112", "image12.jpg"),
    (13, "ВАЗ-2113", "image13.jpg"),
    (14, "ВАЗ-2114", "image14.jpg"),
    (15, "ВАЗ-2115", "image15.jpg"),
    (16, "ИЖ-2715", "image16.jpg"),
    (17, "ИЖ-2717", "image17.jpg"),
    (18, "АЗЛК-412", "image18.jpg"),
    (19, "АЗЛК-2140", "image19.jpg"),
    (20, "ВАЗ-2120", "image20.jpg"),
    (21, "ВАЗ-2121", "image21.jpg"),
    (22, "АЗЛК-2141", "image22.jpg"),
    (23, "ВАЗ-2123", "image23.jpg"),
    (24, "ВАЗ-21123", "image24.jpg"),
    (25, "ИЖ-2125", "image25.jpg"),
    (26, "ИЖ-2126", "image26.jpg"),
    (27, "ВАЗ-211061", "image27.jpg"),
    (28, "ГАЗ-3102", "image28.jpg"),
    (29, "ВАЗ-2129", "image29.jpg"),
    (30, "ГАЗ-2402", "image30.jpg"),
    (31, "ВАЗ-2131", "image31.jpg")
""")
con.commit()