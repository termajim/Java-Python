# Lentopelin tietokantaa ja Flask ohjelmaa käyttäen luodaan taustapalvelu

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_airport_by_icao(icao):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='apina5223',
        autocommit=True
    )
    cursor = yhteys.cursor()
    sql = f'SELECT name, municipality FROM airport WHERE ident = "{icao}";'
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    yhteys.close()
    return result


@app.route('/kenttä/<string:icao>', methods=['GET'])
def get_airport(icao):
    """Palauttaa JSON-muotoisen vastauksen lentokentän tiedoista ICAO-koodin perusteella."""
    airport_data = get_airport_by_icao(icao)

    if airport_data:
        response = {
            "ICAO": icao,
            "Name": airport_data[0],
            "Municipality": airport_data[1]
        }
        return jsonify(response)
    else:
        return jsonify({"error": "Kenttää ei löydy"}), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)
