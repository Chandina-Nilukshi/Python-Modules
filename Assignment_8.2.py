import mysql.connector

def airport_info(country):
    sql = f"SELECT type, COUNT(*) from airport WHERE iso_country = '{country}' group by type order by type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return(result)


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

area_code = input("Enter the area code: ")
airports = airport_info(area_code)

if count is not None:
    print(f"Area {area_code} has : {airports} airports")
else:
    print("No airports were found in this country")

connection.close()
