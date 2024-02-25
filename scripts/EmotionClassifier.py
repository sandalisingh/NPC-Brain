import joblib
from States import get_emotion

# Load the saved model
model = joblib.load('scripts/emotion_classifier_model.joblib')

def emotion_classifier(text):
    predicted_emotion_index = model.predict([text])[0]
    predicted_emotion = get_emotion(predicted_emotion_index)
    print("Emotion :", predicted_emotion)
    return predicted_emotion

