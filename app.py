from flask import Flask, request, jsonify
from main_pipeline import run_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return {"status": "running", "message": "Data Quality Agent Ready 🚀"}

@app.route("/", methods=["POST"])
def process():
    input_data = request.json
    result = run_pipeline(input_data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0")
