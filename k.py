import sqlite3

try:
    # Establish a database connection
    db = sqlite3.connect("mydatabase")  # Replace with your database file name if needed
    print("Connection successful")

    # Create a cursor object
    cur = db.cursor()

    # Uncomment these lines if the table does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS students (Rollno INT PRIMARY KEY, name TEXT)")
    print("Table created....")

    # Clean up the table by deleting existing records
    cur.execute("DELETE FROM students")
    db.commit()
    print("Existing records deleted....")

    # Define the query and data
    query = "INSERT INTO students (Rollno, name) VALUES (?, ?)"
    lst = [(1, "sushanth"), (2, "ameesh"), (3, "Tanish"), (4, "suma")]

    # Insert the new records
    cur.executemany(query, lst)
    db.commit()
    print("Records inserted successfully!!")

    # Fetch and display the records
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)

except sqlite3.Error as err:
    print(f"Error: {err}")
finally:
    # Close the database connection
    if db:
        db.close()
