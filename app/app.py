from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def health():
    return jsonify(({"status":"success",'message':"Server up and running"}), 200)