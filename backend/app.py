from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello from the Flask backend!'})

# Add additional API endpoints here

if __name__ == '__main__':
    app.run(debug=True)
