from EmotionClassifier import emotion_classifier
from States import get_emotion

text = input("Text : ")
print("Test Emotion :", emotion_classifier(text))