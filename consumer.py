import mysql.connector

conn = mysql.connector.connect(
    host="34.130.39.178",
    user="usr",
    password="sofe4630u",
    database="Readings"
)

cursor = conn.cursor(dictionary=True)

cursor.execute("""
    SELECT *
    FROM LabelsData
    ORDER BY ID DESC
    LIMIT 10
""")

rows = cursor.fetchall()

print("Latest stored records:")

for row in rows:
    print(row)

cursor.close()
conn.close()