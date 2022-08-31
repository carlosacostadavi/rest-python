from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def server_info():
    person = {
        "nombre":"Andres",
        "apellido":"Acosta"
    }

    return jsonify(person)

if __name__ == "__main__":
    app.run()