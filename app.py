from flask import Flask, jsonify, request
from repository import StockRepository

app = Flask(__name__)

@app.route('/checktel_and_retrieve_username', methods=['POST'])
def checktel_and_retrieve_username():
    check = StockRepository.check_tel(request.get_json()["user_tel"])
    if check != "":
        json_response = check["name"]+" "+check["surname"]
        return jsonify({"have_account": True, "user_name": json_response})
    else:
        return jsonify({"have_account": False})

@app.route('/newuser_register', methods=['POST'])
def newuser_register():
    json_response = StockRepository.add_user(request.get_json())
    return jsonify({"message": json_response})

@app.route('/')
def hello():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)    