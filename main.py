from flask import Flask, send_file, request, jsonify

app = Flask(__name__, static_url_path="/")

response = {"name": "John"}


@app.route("/")
def welcome():
    return send_file("./static/index.html")


@app.get("/api/name")
def get_name():
    return jsonify(response)


@app.post("/api/name")
def set_name():
    response["name"] = request.json["name"]
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
