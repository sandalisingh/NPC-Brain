import joblib

# Load the saved model
model = joblib.load('emotion_classifier_model.joblib')

def emotion_classifier(text):
    predicted_emotion_index = model.predict([text])[0]
    predicted_emotion = emotion_mapping[predicted_emotion_index]
    print("Emotion :", predicted_emotion)
    return predicted_emotion