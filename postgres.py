import psycopg2

# Connect to PostgreSQL
connection = psycopg2.connect(
    dbname="query_less",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

# Create a cursor object to insert record, create table
cursor = connection.cursor()


# table_info = """
# CREATE TABLE Teacher(
#     NAME VARCHAR(25),
#     CLASS VARCHAR(25),
#     SECTION VARCHAR(25)
# );
# """
# cursor.execute(table_info)

# Insert Some more records
# cursor.execute('''INSERT INTO STUDENT VALUES('Suhel','Data Science','B')''')
# cursor.execute('''INSERT INTO STUDENT VALUES('Raziq','AIML','c')''')
cursor.execute('''INSERT INTO Teacher VALUES('Raziq','AIML','c')''')
cursor.execute('''INSERT INTO Teacher VALUES('Raziq','AIML','c')''')



# Display All the records
print("The inserted records are")
cursor.execute('''SELECT * FROM STUDENT''')
for row in cursor.fetchall():
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
