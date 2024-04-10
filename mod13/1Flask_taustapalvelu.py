# Tehdään Flask taustapalvelu missä käytetään. Parametrit ja luku arvot.
from flask import Flask, jsonify

app = Flask(__name__)
def is_prime(i):
    if i <= 1:
        return False
    if i <= 3:
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    i = 5
    while i * i <= i:
        if i % i == 0 or i % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/alkuluku/<int:number>', methods=['GET'])
def alkuluku(number):
    is_prime_result = is_prime(number)
    response = {
        "Number": number,
        "is_prime": is_prime_result
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=3000)