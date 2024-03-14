from flask import Flask, jsonify, request
from NPC_Brain import NPC_Brain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

NPC = None

@app.route('/')
def hello_world():
    return jsonify('Welcome to NPC world!')

@app.route('/initialize', methods=['POST'])
def initialize_NPC():
  try:
    print("DATA RECEIVED")
    print(response)
    print(response.get_json())
    data = request.get_json()  # Access the data as a dictionary
    environment = data['environment']
    personality_vector = data['personality_vector']
    NPC = NPC_Brain(personality_vector, environment)
    print("Initialized NPC")
    print(NPC_Brain)
    return jsonify({'message': 'Data received successfully!'}), 200  # Return success message

  except Exception as e:
    return jsonify({'error': str(e)}), 400  # Return error response

# Add additional API endpoints here

if __name__ == '__main__':
    app.run(debug=True)
