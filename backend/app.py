import os
from flask import Flask, jsonify, request, session, Response
from NPC_Brain import NPC_Brain
from flask_cors import CORS, cross_origin
from flask_session import Session
import yaml

def load_config():
    with open('config.yaml', 'r') as config_file:
        config = yaml.safe_load(config_file)
    return config

# Load the secret key from config.yaml
config = load_config()
secret_key = config.get('secret_key')
if not secret_key:
    raise RuntimeError("Secret key is not defined in config.yaml")

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['CORS_HEADERS'] = 'Content-Type, Access-Control-Allow-Credentials'
app.config['SECRET_KEY'] = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = True  # Set session as permanent
app.config['SESSION_COOKIE_SECURE'] = True  # Ensure cookie is sent only over HTTPS
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Ensure cookie is only accessible via HTTP(s)
app.config['SESSION_COOKIE_SAMESITE'] = 'Strict'  # Apply strict same-site policy

Session(app)  # Initialize Flask-Session

# npc_brain = NPC_Brain()

@app.route('/')
def npc_world():
    return jsonify('Welcome to NPC world!')

@app.route('/initialize', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def initialize():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    try:
        data = request.get_json()
        environment = data['environment']
        personality_vector = data['personality_vector']

        npc_brain = NPC_Brain(personality_vector, environment)
        emoji = npc_brain.get_emoji()
        emotion = str(npc_brain.get_current_emotion_state())
        action = str(npc_brain.get_current_action_state())

        response = jsonify({
            'emoji': emoji,
            'emotion': emotion,
            'action': action
        })

        session['npc_brain'] = npc_brain
        session.modified = True

        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_response', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def get_response():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    try:
        # session_id = request.cookies.get('session')

        # if session_id:
        #     session.sid = session_id

        print(f"Session ID: {session.sid}")
        print(f"Session: {session}")

        npc_brain = session.get('npc_brain')

        # Check if npc_brain is None
        if npc_brain is None:
            raise Exception("NPC Brain not initialized")

        data = request.get_json()
        chat = data['chat']

        reply = npc_brain.generate_reply(chat)
        emoji = str(npc_brain.get_emoji())
        action = str(npc_brain.get_current_action_state())

        response = jsonify({
            'reply': reply, 
            'emoji': emoji,
            'action': action
        })

        session['npc_brain'] = npc_brain
        session.modified = True

            # print(f"Session ID: {session.sid}")
            # print(f"Session: {session}")

        return response, 200
        # else:
        #     raise Exception("Session ID not found in cookie")

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_states', methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def get_states():
    if request.method == 'OPTIONS':
        response = Response()
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    try:
        # session_id = request.cookies.get('session')
        # session.sid = session_id

        # print(f"Session ID: {session.sid}")
        # print(f"Session: {session}")

        npc_brain = session.get('npc_brain')

        # Check if npc_brain is None
        if npc_brain is None:
            raise Exception("NPC Brain not initialized")

        emoji = str(npc_brain.get_emoji())
        action = str(npc_brain.get_current_action_state())

        response = jsonify({
            'emoji': emoji,
            'action': action
        })

        # response.set_cookie('session', session.sid, secure=True, httponly=True, samesite='Strict')

        session['npc_brain'] = npc_brain
        session.modified = True

        # print(f"Session ID: {session.sid}")
        # print(f"Session: {session}")

        return response, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
