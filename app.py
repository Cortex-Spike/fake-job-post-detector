from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "Backend is running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")

    if "payment" in text.lower() or "fee" in text.lower():
        result = "Fake Job Post"
    else:
        result = "Likely Genuine"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=9001,
        debug=False,
        use_reloader=False
    )
