from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})

# GET endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({
        "message": "Hello from Python server"
    })

# POST endpoint
@app.route('/data', methods=['POST'])
def receive_data():
    payload = request.json
    return jsonify({
        "status": "received",
        "data": payload
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
