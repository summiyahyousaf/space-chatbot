from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import json

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def chatbot_response():
    user_message = request.json["message"]

    response = get_response(user_message)

    return jsonify({"response": response})

@app.route("/history")
def history():

    with open("../data/history.json") as file:
     return json.load(file)


if __name__ == "__main__":
    app.run(debug=True)