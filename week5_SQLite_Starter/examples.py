import sqlite3

conn = sqlite3.connect("polyglot.db")
cursor = conn.cursor()
cursor.execute("UPDATE languages SET answered = 1 WHERE language = \"C++\"")
cursor.execute("INSERT INTO languages (id, language, answer, answered, guide) VALUES (9, \"PHP\", \"$$$\",0 , \"Can you handle this\")")
cursor.execute("DELETE FROM languages WHERE language = \"Ruby\"")
result = cursor.execute("SELECT id, language, answered FROM languages")

for row in result:
    print(row)