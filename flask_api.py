from flask import Flask, jsonify
app = Flask(__name__)

hello_api = {
        'greeting' : "Hello!"
    }

@app.route("/")
def hello():

    return jsonify(hello_api)

if __name__ == '__main__':
    app.run(debug=True)