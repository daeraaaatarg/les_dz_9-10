# БД - База Даних
# мова sql
import sqlite3

connection = sqlite3.connect("database_test.sl3", 5)
cur = connection.cursor()
# ДІЯ - великими; назв_а - без пробілів, малими
#cur.execute("CREATE TABLE first_table (name TEXT);")
#cur.execute("INSERT INTO first_table (name) VALUES ('Ira');")
#cur.execute("INSERT INTO first_table (name) VALUES ('Ivan');")
#cur.execute("INSERT INTO first_table (name) VALUES ('Andriy');")
#cur.execute("SELECT rowid, name FROM first_table;")
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
#cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=3;")
#cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
#cur.execute("DELETE FROM first_table WHERE rowid=2;")
#cur.execute("SELECT rowid, name FROM first_table;")
#cur.execute("DROP TABLE first_table;")

connection.commit()

# res = cur.fetchall()
# print(res)
connection.close()