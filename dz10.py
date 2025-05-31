import sqlite3

connection = sqlite3.connect("FruitBasket.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS fruits (name TEXT, colour TEXT);")

cur.execute("INSERT INTO fruits (name, colour) VALUES ('Apple', 'Red');")
cur.execute("INSERT INTO fruits (name, colour) VALUES ('Banana', 'Yellow');")
cur.execute("INSERT INTO fruits (name, colour) VALUES ('Orange', 'Orange');")

cur.execute("UPDATE fruits SET colour='Green' WHERE colour='Red';")

cur.execute("SELECT rowid, name, colour FROM fruits WHERE colour='Yellow';")
yellows = cur.fetchall()
print("Yellow fruits:")
for y in yellows:
    print(y)

cur.execute("SELECT rowid, name, colour FROM fruits;")
all_fruits = cur.fetchall()
print("\nAll fruits:")
for a in all_fruits:
    print(a)

connection.commit()
connection.close()