from flask import Flask, jsonify, request 
from flask_cors import CORS
from repository import StockRepository

app = Flask(__name__)
CORS(app)

@app.route('/checktel_and_retrieve_username', methods=['POST'])
def checktel_and_retrieve_username():
    check = StockRepository.retrieve_profile(request.get_json()["user_tel"])
    if check != None:
        json_response = check["name"]+" "+check["surname"]
        return jsonify({"have_account": True, "user_name": json_response})
    else:
        return jsonify({"have_account": False})

@app.route('/newuser_register', methods=['POST'])
def newuser_register():
    json_response = StockRepository.add_user(request.get_json())
    return jsonify({"message": json_response})

@app.route('/retrieve_profile', methods=['POST'])
def retrieve_profile():
    json_response = StockRepository.retrieve_profile(request.get_json()["user_tel"])
    return jsonify({"message": json_response})

@app.route('/update_profile', methods=['POST'])
def update_profile():
    json_response = StockRepository.update_profile(request.get_json())
    return jsonify({"message": json_response})


if __name__ == "__main__":
    app.run(debug=True)    