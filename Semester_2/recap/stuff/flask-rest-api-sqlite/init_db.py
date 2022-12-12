import sqlite3

drop_table = """
DROP TABLE IF EXISTS countries;
"""

create_table = """
CREATE TABLE countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    name TEXT NOT NULL,
    capital TEXT NOT NULL,
    area INTEGER NOT NULL
);
"""

with sqlite3.connect('/Semester_2/recap/stuff/flask-rest-api-sqlite/database.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)
    cur.execute("INSERT INTO countries (name, capital, area) VALUES (?, ?, ?);",
                ('Thailand', 'Bangkok', 513120))
    cur.execute("INSERT INTO countries (name, capital, area) VALUES (?, ?, ?);",
                ('Australia', 'Canberra', 7617930))
    cur.execute("INSERT INTO countries (name, capital, area) VALUES (?, ?, ?);",
                ('Egypt', 'Cairo', 1010408))

