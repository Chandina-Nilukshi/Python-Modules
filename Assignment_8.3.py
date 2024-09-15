from multiprocessing import connection
from geopy.distance import geodesic
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

def coordinates(icao_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}';"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    if result:
        return (result[0], result[1])
    else:
        print("Data cannot be found for the given icao_code")
        return None
connection.close()

def distance(icao_code1, icao_code2):
    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    if coordinates1 and coordinates2:
        distance_km = geodesic(coordinates1, coordinates2).kilometers
        print(f"The distance between {icao_code1} and {icao_code2} is {distance_km:.2f} km.")
    else:
        print("Unable to calculate the distance due to missing data.")

if __name__ == "__main__":
    icao_code1 = input("Enter the ICAO code of the first airport: ").upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").upper()

    calculate_distance(icao_code1, icao_code2)