import json
from flask import Flask, render_template, request
from data_handler import get_threat_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        query = request.form["query"].strip()
        query_type = request.form["type"]
        result = get_threat_data(query, query_type)

    return render_template('index.html', result=json.dumps(result, indent=4))

if __name__ == "__main__":
    app.run(debug=True)
