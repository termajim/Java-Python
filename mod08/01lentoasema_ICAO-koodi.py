import mysql.connector

def get_airport_by_icao(icao):
    sql = f'select name, municipality from airport where ident = "EFHK";'
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)
    return result

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='ihmiset',
         user='root',
         password='root',
         autocommit=True
         )

icao = input("Anna ICAO-koodi")

airport = get_airport_by_icao(icao)

print(airport)
print(f"nimi: {airport[0][0]}, joka sijaitsee kunnassa {airport[0][1]}")
