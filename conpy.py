from flask import Flask, request, jsonify
from flask_cors import CORS
from connection import insert_data_psqi

app = Flask(__name__)


CORS(app)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 200


@app.route("/get_person", methods=["GET"])
def get_name():
    user = {
        "name": "john",
        "age" : 30,
        "weigt": 60.5,
        "hight": 150
    }
    return jsonify(user), 200

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json  # ดึงข้อมูล JSON ที่ส่งมาจาก Postman
    print(data)  # แสดงข้อมูลใน console เพื่อตรวจสอบ

# เข้าถึงข้อมูลใน data
    ID = data.get('ID')
    sex = data.get('sex')
    ofAge = data.get('ofAge')
    year = data.get('year')
    numoflearn = data.get('numoflearn')
    learnforweek = data.get('learnforweek')



    # สามารถทำอย่างอื่นต่อจากนี้ เช่น เซฟข้อมูลลงในฐานข้อมูล ประมวลผล ฯลฯ
    insert_data_psqi(ID, sex, ofAge, year, numoflearn, learnforweek);
    return 'Data received successfully', 200



if __name__ == "__main__":
    app.run(debug=True)
