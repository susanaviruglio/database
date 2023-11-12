# important not to call this file or any file as psychopg2 because python will
#  get confuse and it would try to start both files.
import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# built a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all records from all the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen"
#  from the "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Query 7 - select only by "ArtistId" #50 from the "Artist" table
# cursor.execute
# ('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [50]) # Metallica

# Query 8 - select all tracks where the composer
#  is "Metallica" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Metallica"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the results (single)
#results = cursor.fetchone()

#close the connection
connection.close()

# print results
for result in results:
    print(result)