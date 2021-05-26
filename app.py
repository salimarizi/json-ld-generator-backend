from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
import json
from controller.JSONLDController import ProcessingSchema

app = Flask(__name__)
CORS(app)

@app.route("/")
def main():
    # return render_template('index.html')
    return "OK"

@app.route('/schema', methods=['POST'])
def schema_process():
    ps = ProcessingSchema()
    return json.dumps(ps.main(request), indent = 2)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
