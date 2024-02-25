from enum import Enum

class ActionStates(Enum):
    Patrolling = 0
    Attacking = 1
    Fleeing = 2
    Alerted = 3
    Searching = 4
    Interacting = 5
    Resting = 6
    Following = 7
    Celebrating = 8
    Helping = 9

class PersonalityIndex(Enum):
    Openness = 0
    Conscientiousness = 1
    Extraversion = 2
    Agreeableness = 3
    Neuroticism = 4

class Range(Enum):
    Low = range(0, 4)      
    Medium = range(4, 8)   
    High = range(8, 11)

class EmotionStates(Enum):
    Admiration = 0
    Amusement = 1
    Anger = 2
    Annoyance = 3
    Approval = 4
    Caring = 5
    Confusion = 6
    Curiosity = 7
    Desire = 8
    Disappointment = 9
    Disapproval = 10
    Disgust = 11
    Embarrassment = 12
    Excitement = 13
    Fear = 14
    Gratitude = 15
    Grief = 16
    Joy = 17
    Love = 18
    Nervousness = 19
    Optimism = 20
    Pride = 21
    Realization = 22
    Relief = 23
    Remorse = 24
    Sadness = 25
    Surprise = 26
    Neutral = 27

# Function to get emotion from index
def get_emotion(index):
    for emotion in EmotionStates:
        if emotion.value == index:
            return emotion.name
    return None

def get_emoji(emotion):
    emojis = {
        EmotionStates.Amiration: '😊',
        EmotionStates.Amusement: '😄',
        EmotionStates.Anger: '😠',
        EmotionStates.Annoyance: '😒',
        EmotionStates.Approval: '👍',
        EmotionStates.Caring: '❤️',
        EmotionStates.Confusion: '😕',
        EmotionStates.Curiosity: '🤔',
        EmotionStates.Desire: '😏',
        EmotionStates.Disappointment: '😞',
        EmotionStates.Disapproval: '👎',
        EmotionStates.Disgust: '🤢',
        EmotionStates.Embarrassment: '😳',
        EmotionStates.Excitement: '😃',
        EmotionStates.Fear: '😨',
        EmotionStates.Gratitude: '🙏',
        EmotionStates.Grief: '😢',
        EmotionStates.Joy: '😂',
        EmotionStates.Love: '😍',
        EmotionStates.Nervousness: '😰',
        EmotionStates.Optimism: '😊',
        EmotionStates.Pride: '🦁',
        EmotionStates.Realization: '😮',
        EmotionStates.Relief: '😅',
        EmotionStates.Remorse: '😔',
        EmotionStates.Sadness: '😢',
        EmotionStates.Surprise: '😲',
        EmotionStates.Neutral: '😐',
    }
    return emojis.get(emotion, '')

def get_perception(emotion):
    perceptions = {
        EmotionStates.Amiration: "I admire.",
        EmotionStates.Amusement: "I find it amusing.",
        EmotionStates.Anger: "I'm angry.",
        EmotionStates.Annoyance: "I'm annoyed.",
        EmotionStates.Approval: "I approve.",
        EmotionStates.Caring: "I care deeply.",
        EmotionStates.Confusion: "I'm confused.",
        EmotionStates.Curiosity: "I'm curious.",
        EmotionStates.Desire: "I desire.",
        EmotionStates.Disappointment: "I'm disappointed.",
        EmotionStates.Disapproval: "I disapprove.",
        EmotionStates.Disgust: "I'm disgusted.",
        EmotionStates.Embarrassment: "I'm embarrassed.",
        EmotionStates.Excitement: "I'm excited.",
        EmotionStates.Fear: "I'm afraid.",
        EmotionStates.Gratitude: "I'm grateful.",
        EmotionStates.Grief: "I'm grieving.",
        EmotionStates.Joy: "I'm filled with joy.",
        EmotionStates.Love: "I'm in love.",
        EmotionStates.Nervousness: "I'm nervous.",
        EmotionStates.Optimism: "I'm optimistic.",
        EmotionStates.Pride: "I'm proud.",
        EmotionStates.Realization: "I've realized.",
        EmotionStates.Relief: "I feel relieved.",
        EmotionStates.Remorse: "I feel remorseful.",
        EmotionStates.Sadness: "I'm sad.",
        EmotionStates.Surprise: "I'm surprised.",
        EmotionStates.Neutral: "I feel neutral.",
    }
    return perceptions.get(emotion, '')
