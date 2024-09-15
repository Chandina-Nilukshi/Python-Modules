import mysql.connector

def airport_info(icao_code):
    sql = f"SELECT name, municipality from airport WHERE ident = '{icao_code}'"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return (result)


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='root',
         charset='utf8mb4',
         collation='utf8mb4_general_ci',
         autocommit=True
         )

icao_code = input("Enter the icao code: ")
airport = airport_info(icao_code)

if info is not None:
    print(f"{airport} is located")
else:
    print("Airport cannot be found")

connection.close()