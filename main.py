from flask import Flask, send_file, request

app = Flask(__name__, static_url_path="/")

name = {"text": "John"}


@app.route("/")
def welcome():
    return send_file("./static/index.html")


@app.get("/api/name")
def get_name():
    return name["text"]


@app.post("/api/name")
def set_name():
    print(request.data)
    name["text"] = request.data
    return name["text"]


if __name__ == "__main__":
    app.run(debug=True)
