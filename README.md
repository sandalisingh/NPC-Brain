# Project Name - Moody (NPC Brain)

## Description

This repository contains the code for an AI project aimed at creating emotionally intelligent non-player characters (NPCs) for use in various applications such as gaming, virtual assistants, and more. The project utilizes machine learning techniques to imbue NPCs with the ability to recognize and respond to emotions.

## Output screenshots

![WhatsApp Image 2024-04-09 at 23 16 36](https://github.com/sandalisingh/NPC-Brain/assets/77054645/e9b38a26-8055-49e9-9d27-6c0536ef9a62)
![WhatsApp Image 2024-04-09 at 23 17 16](https://github.com/sandalisingh/NPC-Brain/assets/77054645/074932ca-69db-4668-b329-072973258dc9)

## Technologies Used

- React: 18.2.0
- Python: 3.11.8
- Flask: 3.0.2
- Keras: 2.15.0
- TensorFlow: 2.15.0

## Note
Due to their large size, the following model files are not included in the repository but are required for full functionality:
- Action_Q_Table.npy
- dialogue_generator_model.keras
- emotion_classifier_model.joblib
- tokenizer.pkl
Please contact at the below mentioned email to obtain these files.

## Set up

1. Backend Configuration:
- Create a config.yaml file in the backend directory.
- Add a secret_key for your backend session to the config.yaml file.
2. Model Placement:
- Place the required model files in the backend/models directory.

## Project structure

├── backend/
│   ├── models/
│   │   ├── Action_Q_Table.npy 
│   │   ├── dialogue_generator_model.keras
│   │   ├── emotion_classifier_model.joblib
│   │   └── tokenizer.pkl
│   ├── ActionGenerator.py
│   ├── app.py
│   ├── config.yaml
│   ├── DataManager.py
│   ├── DataVisualizer.py
│   ├── DialogueGenerator.py
│   ├── EmotionClassifier.py
│   ├── EmotionGenerator.py
│   ├── NPC_Brain.py
│   ├── PositionalEncoding.py
│   ├── States.py
│   ├── Test_ActionGenerator.py
│   ├── Test_DialogueGenerator.py
│   ├── Test_EmotionClassifier.py
│   ├── Test_EmotionGenerator.py
│   ├── Test_NPC_Brain.py
│   └── Test_Tokenizer.py
└── frontend/
    ├── public/
    ├── src/
    │   ├── Components/
    │   ├── App.css
    │   ├── App.js
    │   └── index.js
    ├── package-lock.json
    └── package.json

## Usage

### To run individual models
1. Emotion Classifier
- Run Test_EmotionClassifier.py file: `python3 backend/Test_EmotionClassifier.py`
2. Emotion Generator
- Run Test_EmotionGenerator.py file: `python3 backend/Test_EmotionGenerator.py`
3. Action Generator
- Run Test_ActionGenerator.py file: `python3 backend/Test_ActionGenerator.py`
4. Dialogue Generator
- Run Test_DialogueGenerator.py file: `python3 backend/Test_DialogueGenerator.py`
5. NPC Brain
- Run Test_NPC_Brain.py file:  `python3 backend/Test_NPC_Brain.py`

### To start backend server locally
1. Run the python file app.py: `python3 backend/app.py`

### To start frontend
1. Navigate to the frontend directory: `cd frontend`
2. Start the npm server: `npm start`

## Contact Us
If you have any questions, suggestions, or would like to collaborate, feel free to reach out to us via email or through GitHub.

Email - sandalisingh.02@gmail.com

Thank you for your interest in our project!