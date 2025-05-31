import sqlite3

connection = sqlite3.connect("AnimalKingdom.sl3", 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS animals (name TEXT, type TEXT);")

cur.execute("INSERT INTO animals (name, type) VALUES ('Lion', 'Mammal');")
cur.execute("INSERT INTO animals (name, type) VALUES ('Crocodile', 'Reptile');")
cur.execute("INSERT INTO animals (name, type) VALUES ('Eagle', 'Bird');")
cur.execute("INSERT INTO animals (name, type) VALUES ('Turtle', 'Reptile');")
cur.execute("INSERT INTO animals (name, type) VALUES ('Monkey', 'Mammal');")

cur.execute("UPDATE animals SET name='Falcone' WHERE name='Eagle';")

cur.execute("SELECT rowid, name, type FROM animals WHERE type='Mammal';")
mammals = cur.fetchall()
print("Mammals:")
for m in mammals:
    print(m)

cur.execute("SELECT rowid, name, type FROM animals;")
all_animals = cur.fetchall()
print("\nAll Animals:")
for a in all_animals:
    print(a)

connection.commit()
connection.close()
