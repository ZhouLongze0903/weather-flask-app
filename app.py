from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder="static")

tianqikey = os.getenv("22876a8c746b2f788a377c9789d75dc1")

@app.route("/")
def shouye():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/weather")
def chaxun():
    chengshi = request.args.get("city")
    if not chengshi:
        return jsonify({"error": "都市名が必要です"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={chengshi}&appid={tianqikey}&units=metric&lang=ja"

    try:
        res = requests.get(url)
        return jsonify(res.json())
    except:
        return jsonify({"error": "天気情報の取得に失敗しました"}), 500

if __name__ == "__main__":
    app.run(debug=True)